#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "providers.json"
RETIRED = ROOT / "data" / "retired.json"
OMNI = ROOT / "data" / "omniroute-free-catalog.json"
ANTIGRAVITY = ROOT / "data" / "antigravity-free-models.json"
OMNI_MODELS = ROOT / "data" / "omniroute-free-models.json"
OUTPUT = ROOT / "README.md"

ICON = {
    "permanent_free_tier": "♾️",
    "recurring_free_tier": "🔄",
    "free_models": "🆓",
    "free_trial_key": "🧪",
    "monthly_credit": "💵",
    "daily_free_allocation": "📅",
    "free_pool": "🆓",
    "keyless_or_free_token": "🔑",
    "anonymous_free_tier": "👤",
    "self_hosted_free_gateway": "🧭"
}

def access_label(p: dict) -> str:
    if "OmniRoute" in p.get("access_via", []):
        return "OmniRoute integration"
    if p["account_required"] and p["auth"] == "api_key":
        return "Login + API key"
    if p["account_required"]:
        return "Login + token"
    return "No login"

ACCESS = access_label


def model_text(models: list[dict]) -> str:
    chunks = []
    for m in models:
        mid = m["id"]
        mods = ", ".join(m.get("modalities", []))
        extra = f" — {m['rate_limit']}" if m.get("rate_limit") else ""
        chunks.append(f"`{mid}` ({mods}{extra})")
    return "; ".join(chunks)


def card_text(p: dict) -> str:
    if p['card_required'] is True:
        return 'Yes'
    if p['card_required'] is False:
        return 'No'
    return 'Unknown'


def card_icon(p: dict) -> str:
    if p['card_required'] is True:
        return '✅'
    if p['card_required'] is False:
        return '—'
    return '?'


def short_quota(p: dict) -> str:
    s = p["quota_summary"]
    # Keep generated tables readable.
    return s if len(s) <= 150 else s[:147].rstrip() + "…"


def provider_block(p: dict) -> str:
    type_icon = ICON.get(p["free_tier_type"], "•")
    compat = "✅" if p["openai_compatible"] else "—"
    label = "Routes" if p["category"] == "gateway" else "Models"
    if p["category"] == "gateway":
        access = "No OmniRoute account"
    else:
        access = ACCESS(p)
    return "\n".join([
        f"### {type_icon} [{p['name']}]({p['signup_url']}) {p['country_flag']}",
        "",
        f"**Access:** {access} · **Card:** {card_text(p)} · **OpenAI-compatible:** {compat}",
        "",
        p["free_summary"],
        "",
        f"**Quota:** {short_quota(p)}",
        "",
        f"**{'Endpoint' if p.get('endpoint_type') == 'integration_reference' else 'Base URL'}:** `{p['base_url']}`",
        "",
        f"**{label}:** {model_text(p['notable_models'])}",
        *( [f"**Default route:** `{p['default_route']}`", "", "**Route guide:** " + "; ".join(f"`{k}` — {v}" for k, v in p.get('route_guidance', {}).items())] if p.get("category") == "gateway" and p.get("default_route") else [] ),
        "",
        f"**Last verified:** {p['last_verified']} · [{p['verification']} sources]({p['docs_url']})",
    ])


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    retired = json.loads(RETIRED.read_text(encoding="utf-8"))["services"] if RETIRED.exists() else []
    omni = json.loads(OMNI.read_text(encoding="utf-8")) if OMNI.exists() else {"entries": []}
    omni_entries = omni.get("entries", [])
    antigravity = json.loads(ANTIGRAVITY.read_text(encoding="utf-8")) if ANTIGRAVITY.exists() else {"models": [], "additional_models": [], "usage_notes": [], "sources": []}
    omni_models = json.loads(OMNI_MODELS.read_text(encoding="utf-8")) if OMNI_MODELS.exists() else {"entries": [], "counts": {}}
    providers = data["providers"]
    first_party = sorted([p for p in providers if p["category"] == "first_party"], key=lambda x: x["name"].lower())
    inference = sorted([p for p in providers if p["category"] == "inference_provider"], key=lambda x: x["name"].lower())
    gateways = sorted([p for p in providers if p["category"] == "gateway"], key=lambda x: x["name"].lower())
    account_required = sum(bool(p["account_required"]) for p in providers)
    gateway_count = len(gateways)
    omniroute_upstreams = [p for p in providers if "OmniRoute" in p.get("access_via", [])]
    no_card = sum(p["card_required"] is False for p in providers)
    card_unknown = sum(p["card_required"] is None for p in providers)
    openai_compat = sum(bool(p["openai_compatible"]) for p in providers)
    free_models = sum(p["free_tier_type"] in {"free_models", "free_pool", "recurring_free_tier", "permanent_free_tier", "daily_free_allocation"} for p in providers)

    parts = [
        "# 🌐 AI API Atlas",
        "",
        "### The map of the free AI ecosystem.",
        "",
        "> Discover free AI models, APIs, gateways, and coding-agent access paths in one open, machine-readable directory.",
        "",
        "[![Data](https://img.shields.io/badge/data-structured%20JSON-informational)](data/providers.json) [![Free models](https://img.shields.io/badge/free%20model%20records-489-brightgreen)](data/omniroute-free-models.json) [![Last verified](https://img.shields.io/badge/verified-2026--09--20-success)](data/providers.json) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)",
        "",
        "## 🚀 Find free AI without the scavenger hunt",
        "",
        "Free AI changes fast: models disappear, quotas move, cards become required, and old tutorials keep circulating. AI API Atlas tracks the access details developers actually need before they integrate.",
        "",
        "**489 OmniRoute free-model catalog records · 35 curated providers/gateways · exact model IDs · quotas · auth requirements · OpenAI compatibility · verification sources**",
        "",
        "[Browse providers](#provider-apis) · [Browse 489 free-model records](data/omniroute-free-models.json) · [Contribute](CONTRIBUTING.md)",
        "",
        "## ⚡ What you get",
        "",
        "This directory deliberately includes **free APIs that require an account/login**. Login-required access is not treated as a worse class of API: it is tracked separately so you can filter by the setup you are willing to accept.",
        "",
        f"**{len(providers)} entries · {gateway_count} gateway · {len(omniroute_upstreams)} OmniRoute upstreams · {account_required} account-required · {no_card} with no card documented · {card_unknown} card requirements unknown · {openai_compat} OpenAI-compatible · {free_models} recurring/model-free entries**",
        "",
        "| Provider | Free access | Account | Card | OpenAI-compatible | Quota |",
        "|---|---|---:|---:|---:|---|",
    ]
    for p in providers:
        access = "OmniRoute" if "OmniRoute" in p.get("access_via", []) else ("login" if p["account_required"] else "anonymous")
        parts.append(
            f"| [{p['name']}]({p['signup_url']}) | {ICON.get(p['free_tier_type'], '•')} {access} | {'✅' if p['account_required'] else '—'} | {card_icon(p)} | {'✅' if p['openai_compatible'] else '—'} | {short_quota(p)} |"
        )

    parts += [
        "",
        "## 🧑‍💻 Free APIs that require login",
        "",
        "These entries provide free API access after account creation and/or key issuance.",
        "",
        "| Provider | Access | Card | Free tier |",
        "|---|---|---|---|",
    ]
    parts.extend([
        f"| [{p['name']}]({p['signup_url']}) | {ACCESS(p)} | {card_text(p)} | {ICON.get(p['free_tier_type'], '•')} {p['free_summary']} |"
        for p in providers if p['account_required'] and "OmniRoute" not in p.get("access_via", [])
    ])
    parts += [
        "",
        "## 🔎 How to use the data",
        "",
        "The README is generated from `data/providers.json`. The structured dataset is the source of truth, so scripts, dashboards, MCP servers, CLIs, and other tools can consume it directly.",
        "",
        "```bash",
        "curl -L https://raw.githubusercontent.com/Vaibhavs25/free-ai-apis-llm/main/data/providers.json",
        "```",
        "",
        "Example fields include `account_required`, `card_required`, `free_tier_type`, `free_summary`, `quota_summary`, `openai_compatible`, `notable_models`, `last_verified`, and `sources`.",
        "",
        "## 🧭 Directory",
        "",
        "- [Provider APIs](#provider-apis)",
        "- [Inference providers](#inference-providers-and-gateways)",
        "- [Gateways and routers](#gateways-and-routers)",
        "- [OmniRoute upstreams](#omniroute-upstreams)",
        "- [Google Antigravity free models](#google-antigravity-free-models)",
        "- [Verification model](#verification-model)",
        "- [Contributing](CONTRIBUTING.md)",
        "- [Security](SECURITY.md)",
        "- [Data schema](data/providers.json)",
        "- [Interactive dashboard](docs/index.html)",
        "",
        "## Provider APIs",
        "",
        "These providers operate their own models or first-party API products.",
        "",
    ]
    parts.append("\n\n".join(provider_block(p) for p in first_party))

    parts += [
        "",
        "## Inference providers and gateways",
        "",
        "These platforms host or expose models from multiple sources.",
        "",
        "\n\n".join(provider_block(p) for p in inference),
        "",
        "## Gateways and routers",
        "",
        "Self-hosted or routing layers are listed separately from direct model providers. Their free capacity depends on the upstream providers you connect; they are not counted as an independent free-token pool.",
        "",
        "\n\n".join(provider_block(p) for p in gateways),
        "",
        "## OmniRoute upstreams",
        "",
        "These are provider integrations that OmniRoute documents as free upstream paths. They are listed separately so the atlas does not imply that OmniRoute itself creates provider quota or that the upstream's direct API terms are identical to its OmniRoute adapter path.",
        "",
        "| Upstream | OmniRoute access | Free classification | Direct API note |",
        "|---|---|---|---|",
    ]
    parts.extend([
        f"| [{p['name']}]({p['signup_url']}) | ✅ | {ICON.get(p['free_tier_type'], '•')} {p['free_tier_type']} | {p.get('direct_api_status','see provider docs')} |"
        for p in omniroute_upstreams
    ])
    parts += [

        "## OmniRoute free catalog",
        "",
        "OmniRoute's current free-tier catalog is tracked as a discovery snapshot. These provider IDs are not automatically promoted to detailed direct-API records; some are adapters, web tools, trials, regional offers, or terms-sensitive proxy paths.",
        "",
        f"**{len(omni_entries)} OmniRoute catalog provider IDs** · source: [{omni.get('source_url', 'OmniRoute')}]({omni.get('source_url', 'https://github.com/diegosouzapw/OmniRoute')})",
        "",
        "| OmniRoute provider | Free classification | Terms flag | Note |",
        "|---|---|---|---|",
        *[f"| {e['omniroute_id']} | {e['free_type']} | {e['tos']} | {e.get('note','')} |" for e in omni_entries],
        "",
        "## Google Antigravity free models",
        "",
        "Google Antigravity currently lists these models as available on the **$0/month Individual plan**. This is a product-access catalog, not a standalone public inference-API claim.",
        "",
        "| Model | Provider | Type | Free access | Notes |",
        "|---|---|---|---|---|",
        *[f"| {m['id']} | {m['provider']} | {m['kind']} | ✅ Individual | {m.get('notes','')} |" for m in antigravity.get('models', [])],
        "",
        "**Additional product models:** " + ", ".join(f"{m['id']} ({m['provider']}; {m['access']})" for m in antigravity.get('additional_models', [])),
        "",
        "**Usage:** " + " ".join(antigravity.get('usage_notes', [])),
        "",
        "**Sources:** " + "; ".join(f"[{u}]({u})" for u in antigravity.get('sources', [])),
        "",
        "## OmniRoute model-level free catalog",
        "",
        "The machine-readable model catalog below is a snapshot of OmniRoute's hand-curated free-model baseline. It is an **access-path catalog**: the same underlying model can appear through multiple providers/pools, so record count is not the same as unique-model count.",
        "",
        "f\"**{len(omni_models.get('entries', []))} active records · {omni_models.get('counts', {}).get('unique_active_model_ids', 0)} unique active model IDs · {omni_models.get('counts', {}).get('active_providers', 0)} providers** · [full JSON](data/omniroute-free-models.json)\",",
        "",
        "The imported snapshot follows OmniRoute's reproducible release catalog. OmniRoute may publish a different resolved/live count when its Radar overlay or catalog changes; this repository does not fabricate live entries into the static snapshot.",
        "",        "## Verification model",
        "",
        "Every provider entry has a `last_verified` date and one or more source URLs. Free access is classified so a $0 recurring quota is not silently presented as the same thing as a time-limited promotion or a small trial credit.",
        "",
        "### Status meanings",
        "",
        "| Field | Meaning |",
        "|---|---|",
        "| `permanent_free_tier` | Provider describes an ongoing free tier |",
        "| `recurring_free_tier` | Free allocation renews on a recurring basis |",
        "| `free_models` | Specific models are priced at $0 |",
        "| `free_trial_key` | Account receives a free but limited trial key |",
        "| `monthly_credit` | Free account receives a recurring credit allocation |",
        "| `daily_free_allocation` | Free allocation resets daily |",
        "| `free_pool` | Provider maintains a free model pool/router |",
        "| `keyless_or_free_token` | Anonymous access and/or a free token exists |",
        "| `anonymous_free_tier` | Free anonymous API path exists |",
        "| `self_hosted_free_gateway` | Self-hosted gateway whose free capacity comes from connected upstream providers |",
        "",
        "## 🧯 Stale-data defense",
        "",
        "This project also records notable provider retirements so older tutorials and lists can be checked against a maintained record.",
        "",
        "| Service | Retired | Evidence |",
        "|---|---|---|",
    ]
    for r in retired:
        parts.append(f"| {r['name']} | {r['retired_on']} | [Provider notice]({r['source']}) |")

    parts += [
        "",
        "## ⚠️ Important",
        "",
        "Free AI APIs change quickly. Model catalogs, quotas, account requirements, regional availability, and data-use terms can change without notice. Always open the linked provider documentation before using an API in production or sending confidential data.",
        "",
        "This project does not store API keys and never asks contributors to submit secrets. Verification workflows should use repository secrets or public metadata only.",
        "",
        "## Contributing",
        "",
        "Add the provider to `data/providers.json`, include primary evidence, and let CI validate the structure. See [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "## License",
        "",
        "MIT. See [LICENSE](LICENSE).",
        ""
    ]
    OUTPUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Generated README.md from {len(providers)} providers.")


if __name__ == "__main__":
    main()
