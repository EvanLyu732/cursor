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
BEGIN_RECENT_MARKER = "<!-- BEGIN AUTO-GENERATED: recent-papers -->"
END_RECENT_MARKER = "<!-- END AUTO-GENERATED: recent-papers -->"
BEGIN_HOTTEST_MARKER = "<!-- BEGIN AUTO-GENERATED: hottest-papers -->"
END_HOTTEST_MARKER = "<!-- END AUTO-GENERATED: hottest-papers -->"
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

HOTTEST_THEME_KEYWORDS = {
    "Vision-language-action": [
        "vision-language-action",
        "vision language action",
        "vla",
        "action model",
    ],
    "Robot foundation models": [
        "foundation model",
        "generalist",
        "cross-robot",
        "cross-embodiment",
        "policy",
    ],
    "Robot learning": [
        "robot learning",
        "imitation learning",
        "reinforcement learning",
        "diffusion policy",
        "world model",
    ],
    "Manipulation": [
        "manipulation",
        "dexterous",
        "grasp",
        "cloth",
        "tactile",
    ],
    "Benchmarks and datasets": [
        "benchmark",
        "dataset",
        "evaluation",
        "red-teaming",
        "safety",
    ],
    "Embodied agents": [
        "embodied",
        "navigation",
        "spatial memory",
        "interactive",
        "simulator",
    ],
}


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


def fetch_recent_papers(
    cutoff: dt.date,
    per_query: int,
    limit: int | None = None,
) -> list[Paper]:
    seen_urls: set[str] = set()
    papers: list[Paper] = []

    for term in SEARCH_TERMS:
        payload = fetch_url(arxiv_query_url(term, per_query))
        for paper in parse_feed(payload):
            if paper.published < cutoff or paper.url in seen_urls or not is_relevant(paper):
                continue
            seen_urls.add(paper.url)
            papers.append(paper)

        # Be courteous to the public arXiv API between multiple queries.
        time.sleep(3)

    papers.sort(key=lambda paper: (paper.published, paper.title.lower()), reverse=True)
    if limit is None:
        return papers
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


def short_summary(paper: Paper, max_chars: int = 220) -> str:
    summary = html.unescape(paper.summary)
    if not summary:
        return "No summary available from arXiv."

    sentence_match = re.search(r"^(.+?[.!?])(?:\s|$)", summary)
    candidate = sentence_match.group(1) if sentence_match else summary
    if len(candidate) <= max_chars:
        return candidate

    truncated = candidate[: max_chars - 1].rsplit(" ", 1)[0].rstrip()
    return f"{truncated}..."


def search_url(base_url: str, query: str, query_param: str = "q") -> str:
    return f"{base_url}?{urllib.parse.urlencode({query_param: query})}"


def related_links(paper: Paper) -> str:
    first_author = paper.authors[0] if paper.authors else "paper author"
    author_query = f"{first_author} {paper.title} homepage"
    discussion_query = f'"{paper.title}"'
    links = [
        ("author site", search_url("https://duckduckgo.com/", author_query)),
        ("X", search_url("https://x.com/search", discussion_query)),
        ("reddit", search_url("https://www.reddit.com/search/", discussion_query)),
    ]
    return " · ".join(f"[{label}]({url})" for label, url in links)


def matched_themes(paper: Paper) -> list[str]:
    searchable = f"{paper.title} {paper.summary}".lower()
    themes: list[str] = []

    for theme, keywords in HOTTEST_THEME_KEYWORDS.items():
        if any(keyword in searchable for keyword in keywords):
            themes.append(theme)

    return themes


def hotness_score(paper: Paper, today: dt.date) -> int:
    searchable = f"{paper.title} {paper.summary}".lower()
    title = paper.title.lower()
    age_days = max(0, (today - paper.published).days)
    score = max(0, 10 - age_days)

    for keywords in HOTTEST_THEME_KEYWORDS.values():
        for keyword in keywords:
            if keyword in title:
                score += 4
            elif keyword in searchable:
                score += 2

    return score


def hottest_papers(papers: list[Paper], today: dt.date, limit: int) -> list[Paper]:
    return sorted(
        papers,
        key=lambda paper: (
            hotness_score(paper, today),
            paper.published,
            paper.title.lower(),
        ),
        reverse=True,
    )[:limit]


def format_recent_markdown(papers: list[Paper], today: dt.date, cutoff: dt.date) -> str:
    lines = [
        BEGIN_RECENT_MARKER,
        f"Last updated: {today.isoformat()} UTC",
        f"Showing papers published from {cutoff.isoformat()} through {today.isoformat()}.",
        "",
        "| Paper | Summary | Authors | Links | Published |",
        "| --- | --- | --- | --- | --- |",
    ]

    for paper in papers:
        title = escape_link_text(paper.title)
        summary = escape_table_cell(short_summary(paper))
        authors = escape_table_cell(format_authors(paper.authors))
        links = related_links(paper)
        lines.append(
            f"| [{title}]({paper.url}) | {summary} | {authors} | {links} | "
            f"{paper.published.isoformat()} |"
        )

    if not papers:
        lines.append("| No papers found in the configured 10-day window. | - | - | - | - |")

    lines.append(END_RECENT_MARKER)
    return "\n".join(lines)


def format_hottest_markdown(
    papers: list[Paper],
    today: dt.date,
    cutoff: dt.date,
    limit: int,
) -> str:
    lines = [
        BEGIN_HOTTEST_MARKER,
        f"Last updated: {today.isoformat()} UTC",
        f"Selected from papers published from {cutoff.isoformat()} through {today.isoformat()}.",
        "",
        "| Paper | Summary | Why it is hot | Links | Published |",
        "| --- | --- | --- | --- | --- |",
    ]

    for paper in hottest_papers(papers, today=today, limit=limit):
        title = escape_link_text(paper.title)
        summary = escape_table_cell(short_summary(paper))
        themes = matched_themes(paper)
        reason = escape_table_cell(", ".join(themes[:3]) if themes else "High recent relevance")
        links = related_links(paper)
        lines.append(
            f"| [{title}]({paper.url}) | {summary} | {reason} | {links} | "
            f"{paper.published.isoformat()} |"
        )

    if not papers:
        lines.append("| No papers found in the configured 10-day window. | - | - | - | - |")

    lines.append(END_HOTTEST_MARKER)
    return "\n".join(lines)


def replace_section(content: str, begin_marker: str, end_marker: str, generated: str) -> str:
    pattern = re.compile(
        rf"{re.escape(begin_marker)}.*?{re.escape(end_marker)}",
        flags=re.DOTALL,
    )

    if not pattern.search(content):
        raise RuntimeError(f"could not find generated section markers: {begin_marker}")

    return pattern.sub(generated, content)


def update_readme(readme: Path, generated_sections: list[tuple[str, str, str]]) -> bool:
    content = readme.read_text(encoding="utf-8")
    updated = content

    for begin_marker, end_marker, generated in generated_sections:
        updated = replace_section(updated, begin_marker, end_marker, generated)

    if updated == content:
        return False

    readme.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--days",
        type=int,
        default=10,
        help="number of recent publication days to keep, including today",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="optional maximum papers to list; 0 keeps all papers in the date window",
    )
    parser.add_argument(
        "--hot-limit",
        type=int,
        default=5,
        help="number of papers to highlight in the hottest section",
    )
    parser.add_argument(
        "--per-query",
        type=int,
        default=25,
        help="maximum arXiv results to fetch for each search term",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=README,
        help="README file to update",
    )
    args = parser.parse_args()

    if args.days < 1:
        parser.error("--days must be at least 1")
    if args.limit < 0:
        parser.error("--limit must be 0 or greater")
    if args.hot_limit < 1:
        parser.error("--hot-limit must be at least 1")

    today = dt.datetime.now(dt.timezone.utc).date()
    cutoff = today - dt.timedelta(days=args.days - 1)
    limit = args.limit or None
    papers = fetch_recent_papers(cutoff=cutoff, limit=limit, per_query=args.per_query)
    generated_recent = format_recent_markdown(papers, today=today, cutoff=cutoff)
    generated_hottest = format_hottest_markdown(
        papers,
        today=today,
        cutoff=cutoff,
        limit=args.hot_limit,
    )
    changed = update_readme(
        args.readme,
        [
            (BEGIN_HOTTEST_MARKER, END_HOTTEST_MARKER, generated_hottest),
            (BEGIN_RECENT_MARKER, END_RECENT_MARKER, generated_recent),
        ],
    )

    if changed:
        print(
            f"Updated {args.readme} with {len(papers)} papers "
            f"from the last {args.days} days."
        )
    else:
        print(f"{args.readme} is already up to date.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
