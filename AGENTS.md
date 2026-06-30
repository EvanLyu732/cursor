# AGENTS.md

## Cursor Cloud specific instructions

This repository is **"Awesome Embodied Intelligence"**: a zero-build static website plus a
standard-library-only Python content updater. There is **no package manager, lockfile, build
step, backend, or database**. The only runtime requirement is **Python 3** (already present).

### Services

| Service | Required | How to run | Notes |
| --- | --- | --- | --- |
| Static site | Yes (to view the product) | `python3 -m http.server 8000` from repo root, then open `http://localhost:8000/` | `index.html` does `fetch("README.md")`, so it must be served over HTTP — opening via `file://` fails CORS. Needs outbound internet for the jsDelivr CDN (`marked`, `DOMPurify`, `mermaid`); without it the page degrades to showing raw Markdown. |
| Content updater | No (CI cron job) | `python3 scripts/update_recent.py` | Rewrites the `<!-- BEGIN/END AUTO-GENERATED -->` marker sections in `README.md` in place. Needs outbound internet to reach `export.arxiv.org`. Sleeps ~3s between 9 queries, so a full run takes ~30s+. |

### Non-obvious notes

- The updater **edits `README.md` in place**. To test it without dirtying the working tree, run
  it against a copy: `python3 scripts/update_recent.py --readme /tmp/README_test.md`.
- Useful flags for faster test runs: `--days`, `--per-query`, `--hot-limit`, `--idea-limit`,
  `--idea-edge-limit`.
- There is no lint config and no automated test suite in this repo. "Build" in CI is just copying
  `index.html` + `README.md` into `_site/` (see `.github/workflows/deploy-pages.yml`).
