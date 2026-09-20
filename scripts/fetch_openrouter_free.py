#!/usr/bin/env python3
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "generated" / "openrouter-free-models.json"
URL = "https://openrouter.ai/api/v1/models"


def main() -> None:
    req = urllib.request.Request(URL, headers={"User-Agent": "AI-API-Atlas/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)

    models = []
    for m in payload.get("data", []):
        pricing = m.get("pricing") or {}
        if str(pricing.get("prompt")) == "0" and str(pricing.get("completion")) == "0":
            models.append({
                "id": m.get("id"),
                "name": m.get("name"),
                "context_length": m.get("context_length"),
                "architecture": m.get("architecture"),
                "pricing": pricing,
                "top_provider": m.get("top_provider"),
                "last_seen": time.strftime("%Y-%m-%d", time.gmtime()),
            })

    models.sort(key=lambda x: (x.get("name") or x.get("id") or "").lower())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "source": URL,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "count": len(models),
        "models": models
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Captured {len(models)} free OpenRouter models -> {OUT}")


if __name__ == "__main__":
    main()
