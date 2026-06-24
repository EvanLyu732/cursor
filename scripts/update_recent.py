#!/usr/bin/env python3
"""Update the auto-generated recent papers section in README.md.

The script uses the public arXiv Atom API and only Python standard-library
modules so it can run in GitHub Actions without installing dependencies.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"
BEGIN_MARKER = "<!-- BEGIN AUTO-GENERATED: recent-papers -->"
END_MARKER = "<!-- END AUTO-GENERATED: recent-papers -->"
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = {"atom": "http://www.w3.org/2005/Atom"}

SEARCH_TERMS = [
    '"embodied intelligence"',
    '"embodied AI"',
    '"embodied agent"',
    '"robot learning"',
    '"robot manipulation"',
    '"vision-language-action"',
    '"vision language action"',
    '"generalist robot"',
    '"robot foundation model"',
]

RELEVANCE_KEYWORDS = [
    "embodied",
    "robot",
    "robotic",
    "manipulation",
    "locomotion",
    "navigation",
    "vision-language-action",
    "vision language action",
    "vla",
    "affordance",
    "sim-to-real",
    "simulation",
]


@dataclass(frozen=True)
class Paper:
    title: str
    url: str
    authors: tuple[str, ...]
    published: dt.date
    summary: str


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def strip_version(url: str) -> str:
    versionless = re.sub(r"v\d+$", "", url)
    return versionless.replace("http://arxiv.org", "https://arxiv.org")


def fetch_url(url: str, retries: int = 3) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "awesome-embodied-intelligence-updater/1.0 "
            "(https://github.com/EvanLyu732/cursor)"
        },
    )

    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            if attempt == retries:
                raise RuntimeError(f"failed to fetch {url}: {error}") from error
            time.sleep(2**attempt)

    raise RuntimeError(f"failed to fetch {url}")


def arxiv_query_url(term: str, max_results: int) -> str:
    query = urllib.parse.urlencode(
        {
            "search_query": f"all:{term}",
            "start": "0",
            "max_results": str(max_results),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    return f"{ARXIV_API}?{query}"


def parse_arxiv_date(value: str) -> dt.date:
    return dt.datetime.strptime(value[:10], "%Y-%m-%d").date()


def parse_feed(payload: bytes) -> list[Paper]:
    root = ET.fromstring(payload)
    papers: list[Paper] = []

    for entry in root.findall("atom:entry", ATOM):
        title = normalize_whitespace(entry.findtext("atom:title", default="", namespaces=ATOM))
        url = normalize_whitespace(entry.findtext("atom:id", default="", namespaces=ATOM))
        summary = normalize_whitespace(entry.findtext("atom:summary", default="", namespaces=ATOM))
        published_text = normalize_whitespace(
            entry.findtext("atom:published", default="", namespaces=ATOM)
        )
        authors = tuple(
            normalize_whitespace(author.findtext("atom:name", default="", namespaces=ATOM))
            for author in entry.findall("atom:author", ATOM)
        )

        if not title or not url or not published_text:
            continue

        papers.append(
            Paper(
                title=title,
                url=strip_version(url),
                authors=tuple(author for author in authors if author),
                published=parse_arxiv_date(published_text),
                summary=summary,
            )
        )

    return papers


def is_relevant(paper: Paper) -> bool:
    searchable = f"{paper.title} {paper.summary}".lower()
    return any(keyword in searchable for keyword in RELEVANCE_KEYWORDS)


def fetch_recent_papers(limit: int, per_query: int) -> list[Paper]:
    seen_urls: set[str] = set()
    papers: list[Paper] = []

    for term in SEARCH_TERMS:
        payload = fetch_url(arxiv_query_url(term, per_query))
        for paper in parse_feed(payload):
            if paper.url in seen_urls or not is_relevant(paper):
                continue
            seen_urls.add(paper.url)
            papers.append(paper)

        # Be courteous to the public arXiv API between multiple queries.
        time.sleep(3)

    papers.sort(key=lambda paper: (paper.published, paper.title.lower()), reverse=True)
    return papers[:limit]


def format_authors(authors: tuple[str, ...], max_authors: int = 6) -> str:
    if not authors:
        return "Unknown authors"
    if len(authors) <= max_authors:
        return ", ".join(authors)
    remaining = len(authors) - max_authors
    return f"{', '.join(authors[:max_authors])}, et al. (+{remaining})"


def escape_table_cell(value: str) -> str:
    return html.unescape(value).replace("|", "\\|")


def escape_link_text(value: str) -> str:
    return escape_table_cell(value).replace("[", "\\[").replace("]", "\\]")


def format_markdown(papers: list[Paper], today: dt.date) -> str:
    lines = [
        BEGIN_MARKER,
        f"Last updated: {today.isoformat()} UTC",
        "",
        "| Paper | Authors | Published |",
        "| --- | --- | --- |",
    ]

    for paper in papers:
        title = escape_link_text(paper.title)
        authors = escape_table_cell(format_authors(paper.authors))
        lines.append(
            f"| [{title}]({paper.url}) | {authors} | {paper.published.isoformat()} |"
        )

    if not papers:
        lines.append("| No recent papers found by the configured sources. | - | - |")

    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme(readme: Path, generated: str) -> bool:
    content = readme.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}",
        flags=re.DOTALL,
    )

    if not pattern.search(content):
        raise RuntimeError(f"could not find generated section markers in {readme}")

    updated = pattern.sub(generated, content)
    if updated == content:
        return False

    readme.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=12, help="maximum papers to list")
    parser.add_argument(
        "--per-query",
        type=int,
        default=8,
        help="maximum arXiv results to fetch for each search term",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=README,
        help="README file to update",
    )
    args = parser.parse_args()

    papers = fetch_recent_papers(limit=args.limit, per_query=args.per_query)
    generated = format_markdown(papers, today=dt.datetime.now(dt.timezone.utc).date())
    changed = update_readme(args.readme, generated)

    if changed:
        print(f"Updated {args.readme} with {len(papers)} recent papers.")
    else:
        print(f"{args.readme} is already up to date.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
