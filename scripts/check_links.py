#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "providers.json"
TIMEOUT = 15


def check(url: str) -> tuple[bool, int | None, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "AI-API-Atlas-LinkChecker/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return True, resp.status, resp.geturl()
    except urllib.error.HTTPError as exc:
        # A permissions/anti-bot response still proves the URL exists.
        if exc.code in {401, 403, 429}:
            return True, exc.code, str(exc)
        return False, exc.code, str(exc)
    except Exception as exc:
        return False, None, str(exc)


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    urls = []
    for p in data["providers"]:
        urls.extend([p["signup_url"], p["docs_url"], *p["sources"]])
    urls = sorted(set(urls))
    failures = []
    for url in urls:
        if url.startswith("https://api."):
            # API base URLs are intentionally validated separately; providers may return 401 on root endpoints.
            continue
        ok, status, detail = check(url)
        mark = "OK" if ok else "FAIL"
        print(f"[{mark}] {status or '-':>3} {url}")
        if not ok:
            failures.append((url, status, detail))
    if failures:
        print(f"\n{len(failures)} link(s) failed.")
        return 1
    print(f"\nChecked {len(urls)} documentation/access URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
