#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "providers.json"
OMNI = ROOT / "data" / "omniroute-free-catalog.json"

REQUIRED = [
    "id", "name", "category", "signup_url", "docs_url", "base_url", "auth",
    "account_required", "card_required", "free_tier_type", "free_summary",
    "quota_summary", "notable_models", "last_verified", "verification", "sources", "status"
]
VALID_CATEGORIES = {"first_party", "inference_provider", "gateway"}
VALID_FREE_TYPES = {
    "permanent_free_tier", "recurring_free_tier", "free_models", "free_trial_key",
    "monthly_credit", "daily_free_allocation", "free_pool", "keyless_or_free_token",
    "anonymous_free_tier", "self_hosted_free_gateway"
}


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    try:
        payload = json.loads(DATA.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: unable to parse {DATA}: {exc}")
        return 1

    errors: list[str] = []
    providers = payload.get("providers")
    if not isinstance(providers, list) or not providers:
        errors.append("providers must be a non-empty list")
        providers = []

    ids: set[str] = set()
    for idx, provider in enumerate(providers, start=1):
        prefix = f"provider #{idx}"
        if not isinstance(provider, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        for field in REQUIRED:
            if field not in provider:
                errors.append(f"{prefix}: missing required field '{field}'")
        pid = provider.get("id")
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", pid):
            errors.append(f"{prefix}: invalid id {pid!r}")
        elif pid in ids:
            errors.append(f"{prefix}: duplicate id '{pid}'")
        else:
            ids.add(pid)

        if provider.get("category") not in VALID_CATEGORIES:
            errors.append(f"{prefix}: invalid category")
        if provider.get("free_tier_type") not in VALID_FREE_TYPES:
            errors.append(f"{prefix}: invalid free_tier_type")
        if provider.get("account_required") is not True and provider.get("account_required") is not False:
            errors.append(f"{prefix}: account_required must be boolean")
        if provider.get("card_required") is not None and provider.get("card_required") is not True and provider.get("card_required") is not False:
            errors.append(f"{prefix}: card_required must be boolean or null")

        for url_field in ("signup_url", "docs_url", "base_url"):
            value = provider.get(url_field)
            if not isinstance(value, str) or not is_url(value):
                errors.append(f"{prefix}: {url_field} must be an http(s) URL")
        sources = provider.get("sources")
        if not isinstance(sources, list) or not sources or any(not is_url(x) for x in sources):
            errors.append(f"{prefix}: sources must be a non-empty list of http(s) URLs")

        models = provider.get("notable_models")
        if not isinstance(models, list) or not models:
            errors.append(f"{prefix}: notable_models must be non-empty")
        else:
            for m_idx, model in enumerate(models, start=1):
                if not isinstance(model, dict) or not isinstance(model.get("id"), str):
                    errors.append(f"{prefix}: model #{m_idx} needs an id")
                if not isinstance(model.get("modalities"), list) or not model.get("modalities"):
                    errors.append(f"{prefix}: model #{m_idx} needs modalities")

        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(provider.get("last_verified", ""))):
            errors.append(f"{prefix}: last_verified must be YYYY-MM-DD")

    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1


    if OMNI.exists():
        try:
            omni = json.loads(OMNI.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"unable to parse OmniRoute catalog: {exc}")
            omni = {}
        entries = omni.get("entries")
        if not isinstance(entries, list) or not entries:
            errors.append("OmniRoute catalog entries must be a non-empty list")
        seen_omni: set[str] = set()
        for idx, entry in enumerate(entries or [], start=1):
            if not isinstance(entry, dict):
                errors.append(f"OmniRoute entry #{idx} must be an object")
                continue
            oid = entry.get("omniroute_id")
            if not isinstance(oid, str) or not oid:
                errors.append(f"OmniRoute entry #{idx} needs omniroute_id")
            elif oid in seen_omni:
                errors.append(f"OmniRoute entry #{idx}: duplicate id '{oid}'")
            else:
                seen_omni.add(oid)
            if entry.get("free_type") not in {"recurring","uncapped","signup_credit","keyless","one_time"}:
                errors.append(f"OmniRoute entry #{idx}: invalid free_type")
            if entry.get("tos") not in {"ok","caution","ambiguous","avoid","unknown"}:
                errors.append(f"OmniRoute entry #{idx}: invalid tos")

    # Guard against accidentally adding a duplicate source or empty display metadata.
    for provider in providers:
        if provider.get("openai_compatible") is None:
            errors.append(f"{provider.get('name', 'unknown')}: openai_compatible must be explicit")
        if provider.get("access_via") is not None and not isinstance(provider.get("access_via"), list):
            errors.append(f"{provider.get('name', 'unknown')}: access_via must be a list when present")
        if provider.get("endpoint_type") is not None and provider.get("endpoint_type") not in {"upstream_api", "integration_reference", "local_gateway"}:
            errors.append(f"{provider.get('name', 'unknown')}: invalid endpoint_type")
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1

    print(f"Validated {len(providers)} providers successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
