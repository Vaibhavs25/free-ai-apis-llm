# 🌐 AI API Atlas

> A continuously maintained, developer-first directory of AI APIs, free tiers, models, limits, compatibility, and access requirements.

[![Data](https://img.shields.io/badge/data-structured%20JSON-informational)](data/providers.json) [![Last verified](https://img.shields.io/badge/verified-2026--09--20-success)](data/providers.json) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ⚡ What you get

This directory deliberately includes **free APIs that require an account/login**. Login-required access is not treated as a worse class of API: it is tracked separately so you can filter by the setup you are willing to accept.

**35 entries · 1 gateway · 15 OmniRoute upstreams · 27 account-required · 12 with no card documented · 23 card requirements unknown · 31 OpenAI-compatible · 22 recurring/model-free entries**

| Provider | Free access | Account | Card | OpenAI-compatible | Quota |
|---|---|---:|---:|---:|---|
| [Google Gemini API](https://aistudio.google.com/app/apikey) | 🔄 login | ✅ | — | ✅ | Model-specific quotas; current exact limits are shown in the account/AI Studio quota view. |
| [Groq](https://console.groq.com/keys) | 🔄 login | ✅ | — | ✅ | Limits are model and organization specific; the public rate-limit page lists current model ceilings and response headers expose remaining quota. |
| [Cerebras Inference](https://cloud.cerebras.ai/) | 🔄 login | ✅ | ? | ✅ | Exact free-tier limits are account/service dependent; the provider publishes that the Free tier has lower rate limits. |
| [Mistral AI](https://console.mistral.ai/api-keys) | 🔄 login | ✅ | — | ✅ | Monthly included usage and limits are shown in the account Limits/Subscription views. |
| [Cohere](https://dashboard.cohere.com/api-keys) | 🧪 login | ✅ | ? | — | The documented monthly trial limit is 1,000 calls; endpoint-specific limits also apply. |
| [OpenRouter](https://openrouter.ai/keys) | 🆓 login | ✅ | — | ✅ | 50 requests/day on the Free plan; free model availability changes frequently. |
| [Cloudflare Workers AI](https://dash.cloudflare.com/) | 📅 login | ✅ | ? | ✅ | 10,000 Neurons/day shared across Workers AI usage; limits reset daily at 00:00 UTC. |
| [Hugging Face Inference Providers](https://huggingface.co/settings/tokens) | 💵 login | ✅ | ? | ✅ | $0.10/month for Free users; additional usage requires purchased credits or another billing arrangement. |
| [Z AI (Zhipu AI)](https://open.bigmodel.cn/usercenter/apikeys) | 🆓 login | ✅ | ? | ✅ | Limits are model/account specific; published free models may be concurrency limited. |
| [ModelScope API-Inference](https://modelscope.cn/my/myaccesstoken) | 🔄 login | ✅ | ? | ✅ | Published limits include 2,000 requests/day total per user, with per-model quotas dynamically adjusted and capped at 500. |
| [SiliconFlow](https://cloud.siliconflow.cn/account/ak) | 🆓 login | ✅ | ? | ✅ | Free-model rate limits are fixed per model; exact limits are exposed by the model catalog. |
| [Ollama Cloud](https://ollama.com/settings/keys) | 🔄 login | ✅ | ? | ✅ | Session limits reset every five hours and weekly limits reset every seven days; exact model weighting varies. |
| [Kilo Code](https://app.kilo.ai/profile) | 🆓 anonymous | — | ? | ✅ | Published free-gateway access is rate limited; the provider documents 200 requests/hour per IP for the free pool. |
| [LLM7.io](https://token.llm7.io) | 🔑 anonymous | — | — | ✅ | Anonymous: 10 RPM, 60 requests/hour and 500k tokens/day; free-token limits are higher according to the provider's limits page. |
| [OVHcloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) | 👤 anonymous | — | — | ✅ | 2 requests/minute per IP per model on the anonymous free path; higher limits are paid. |
| [Aion Labs](https://www.aionlabs.ai/app/api-keys/) | ♾️ login | ✅ | ? | ✅ | Published limits include 15 RPM and 20K tokens/day on the referenced free endpoints. |
| [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 🧭 anonymous | — | — | ✅ | No separate OmniRoute quota. Available capacity follows the free or paid quotas of the providers you connect; documented routing supports automatic… |
| [Kiro AI (OmniRoute upstream)](https://kiro.dev/) | 🔄 OmniRoute | — | — | — | Kiro Free currently lists 50 credits per monthly billing cycle; exact model/rate consumption depends on the request. OmniRoute may abstract provide… |
| [OpenCode Free (OmniRoute upstream)](https://opencode.ai/) | 🆓 OmniRoute | — | ? | ✅ | Free-model availability and limits are model-specific and can change; current OpenCode documentation lists free models such as MiMo-V2.5 Free, Ling… |
| [Pollinations (OmniRoute upstream)](https://pollinations.ai/) | 🔑 OmniRoute | — | ? | ✅ | No single stable quota is asserted here because Pollinations exposes different free/registered/key-based access paths and model-specific rules; use… |
| [Nara Router](https://router.bynara.id/) | 📅 OmniRoute | ✅ | ? | ✅ | 7M tokens/day and 15 RPM on the currently published Free plan; the daily pool is shared across its free models. |
| [xKiro](https://xkiro.com/) | 📅 OmniRoute | ✅ | — | ✅ | The current documentation exposes a daily account-level free-token allowance; exact limits are returned by the live usage endpoint. |
| [API Airforce](https://api.airforce/) | 📅 OmniRoute | ✅ | ? | ✅ | Published Free plan limit: 1 RPM and 1,000 requests/day. |
| [BazaarLink](https://bazaarlink.ai/en/docs) | 🆓 OmniRoute | ✅ | ? | ✅ | Free routing is subject to the provider's current RPM/daily cap; the live /v1/models catalog marks free models with a :free suffix. |
| [NavyAI](https://api.navy/) | 📅 OmniRoute | ✅ | ? | ✅ | The current public plan page advertises 150K tokens/day and 20 RPM. |
| [AI Horde](https://aihorde.net/register) | 🔑 OmniRoute | — | — | — | Availability and speed depend on the community worker pool rather than a fixed commercial token quota. |
| [SEA-LION API](https://docs.sea-lion.ai/guides/inferencing/api) | 🧪 OmniRoute | ✅ | — | ✅ | 10 requests/minute on the free API; intended for POC use rather than production workloads. |
| [Baidu Qianfan ERNIE](https://console.bce.baidu.com/qianfan/ais/console/apiKey) | ♾️ OmniRoute | ✅ | ? | ✅ | Free RPM/TPM quotas are console-controlled; use the current Qianfan console as the exact source of limits. |
| [DeepSeek API](https://platform.deepseek.com/) | 🧪 OmniRoute | ✅ | — | ✅ | Current catalog evidence records 5M free tokens on signup for a limited period; confirm current account eligibility before relying on it. |
| [Google Cloud Vertex AI](https://console.cloud.google.com/) | 🧪 OmniRoute | ✅ | ? | — | $300 new-customer cloud credit; one-time trial rather than a permanent API quota. |
| [Hyperbolic](https://app.hyperbolic.ai/) | 🧪 OmniRoute | ✅ | ? | ✅ | Signup credit is one-time rather than a recurring free allowance; confirm the live account offer. |
| [LongCat API](https://longcat.ai/platform/) | 🧪 OmniRoute | ✅ | ? | ✅ | Current OmniRoute evidence records a one-time 10M-token free allocation; verify the live LongCat account quota before use. |
| [Morph](https://www.morphllm.com/) | 💵 login | ✅ | ? | ✅ | 200 requests/month free; hosted model usage after the free allowance is usage-priced. |
| [Public AI Gateway](https://platform.publicai.co/) | 🔄 login | ✅ | ? | ✅ | The current Free tier is documented at 100 requests/minute; paid/Plus plans increase that limit. |
| [NVIDIA NIM](https://build.nvidia.com/explore/discover) | 🔄 login | ✅ | ? | ✅ | The reference snapshot lists 40 RPM and 10,000 requests/day for its included models; check the current NVIDIA model page for live limits. |

## 🧑‍💻 Free APIs that require login

These entries provide free API access after account creation and/or key issuance.

| Provider | Access | Card | Free tier |
|---|---|---|---|
| [Google Gemini API](https://aistudio.google.com/app/apikey) | Login + API key | No | 🔄 New Gemini API accounts start on the Free Tier with access to selected models within their model-specific free-tier limits. |
| [Groq](https://console.groq.com/keys) | Login + API key | No | 🔄 Groq exposes a Free tier with model-specific request/token limits; payment information is needed only when upgrading to paid usage. |
| [Cerebras Inference](https://cloud.cerebras.ai/) | Login + API key | Unknown | 🔄 Cerebras offers a $0 Free tier with lower rate limits and community support. |
| [Mistral AI](https://console.mistral.ai/api-keys) | Login + API key | No | 🔄 Mistral Studio starts in Free mode by default, with API access and limited included usage; no credit card is required to activate Studio. |
| [Cohere](https://dashboard.cohere.com/api-keys) | Login + API key | Unknown | 🧪 A Cohere account automatically receives a trial API key. Trial API usage is free but limited. |
| [OpenRouter](https://openrouter.ai/keys) | Login + API key | No | 🆓 OpenRouter's Free plan provides API access to 25+ free models and currently lists a 50 requests/day rate limit. |
| [Cloudflare Workers AI](https://dash.cloudflare.com/) | Login + token | Unknown | 📅 Workers AI is available on Cloudflare's Free plan with 10,000 Neurons/day at no charge. |
| [Hugging Face Inference Providers](https://huggingface.co/settings/tokens) | Login + token | Unknown | 💵 Free Hugging Face users receive $0.10/month in Inference Provider credits, subject to change. |
| [Z AI (Zhipu AI)](https://open.bigmodel.cn/usercenter/apikeys) | Login + API key | Unknown | 🆓 Z AI publishes selected models at Free pricing, including GLM-4.7-Flash and other free variants. |
| [ModelScope API-Inference](https://modelscope.cn/my/myaccesstoken) | Login + token | Unknown | 🔄 ModelScope provides free API-Inference for registered users under published usage/concurrency limits. |
| [SiliconFlow](https://cloud.siliconflow.cn/account/ak) | Login + API key | Unknown | 🆓 SiliconFlow has model-specific free models whose calls are priced at zero after the account requirements are satisfied. |
| [Ollama Cloud](https://ollama.com/settings/keys) | Login + API key | Unknown | 🔄 Ollama Cloud provides a free tier with session and weekly usage limits for supported cloud model families. |
| [Aion Labs](https://www.aionlabs.ai/app/api-keys/) | Login + API key | Unknown | ♾️ Aion Labs advertises a permanent free tier for its text inference APIs. |
| [Morph](https://www.morphllm.com/) | Login + API key | Unknown | 💵 Morph publishes an OpenAI-compatible API with 200 free requests every month. |
| [Public AI Gateway](https://platform.publicai.co/) | Login + API key | Unknown | 🔄 Public AI documents a Free tier with API access to public and sovereign models. |
| [NVIDIA NIM](https://build.nvidia.com/explore/discover) | Login + API key | Unknown | 🔄 NVIDIA NIM provides API access to selected models for NVIDIA Developer Program members, subject to model-specific limits. |

## 🔎 How to use the data

The README is generated from `data/providers.json`. The structured dataset is the source of truth, so scripts, dashboards, MCP servers, CLIs, and other tools can consume it directly.

```bash
curl -L https://raw.githubusercontent.com/Vaibhavs25/free-ai-apis-llm/main/data/providers.json
```

Example fields include `account_required`, `card_required`, `free_tier_type`, `free_summary`, `quota_summary`, `openai_compatible`, `notable_models`, `last_verified`, and `sources`.

## 🧭 Directory

- [Provider APIs](#provider-apis)
- [Inference providers](#inference-providers-and-gateways)
- [Gateways and routers](#gateways-and-routers)
- [OmniRoute upstreams](#omniroute-upstreams)
- [Google Antigravity free models](#google-antigravity-free-models)
- [Verification model](#verification-model)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Data schema](data/providers.json)
- [Interactive dashboard](docs/index.html)

## Provider APIs

These providers operate their own models or first-party API products.

### ♾️ [Aion Labs](https://www.aionlabs.ai/app/api-keys/) 🇮🇱

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

Aion Labs advertises a permanent free tier for its text inference APIs.

**Quota:** Published limits include 15 RPM and 20K tokens/day on the referenced free endpoints.

**Base URL:** `https://api.aionlabs.ai/v1`

**Models:** `aion-labs/aion-2.0` (text); `aion-labs/aion-3.0` (text); `aion-labs/aion-3.0-mini` (text)

**Last verified:** 2026-09-20 · [provider_page_reference sources](https://www.aionlabs.ai/)

### ♾️ [Baidu Qianfan ERNIE](https://console.bce.baidu.com/qianfan/ais/console/apiKey) 🇨🇳

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

Baidu documents long-term free access for selected ERNIE services after real-name verification.

**Quota:** Free RPM/TPM quotas are console-controlled; use the current Qianfan console as the exact source of limits.

**Base URL:** `https://qianfan.baidubce.com/v2`

**Models:** `ernie-speed-8k` (text); `ernie-speed-128k` (text); `ernie-lite-8k` (text)

**Last verified:** 2026-09-20 · [official_provider_announcement sources](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/llf9l3kew)

### 🔄 [Cerebras Inference](https://cloud.cerebras.ai/) 🇺🇸

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

Cerebras offers a $0 Free tier with lower rate limits and community support.

**Quota:** Exact free-tier limits are account/service dependent; the provider publishes that the Free tier has lower rate limits.

**Base URL:** `https://api.cerebras.ai/v1`

**Models:** `gpt-oss-120b` (text); `llama-4-scout-17b-16e-instruct` (text, image); `llama3.1-8b` (text)

**Last verified:** 2026-09-20 · [official_docs sources](https://inference-docs.cerebras.ai/quickstart)

### 🧪 [Cohere](https://dashboard.cohere.com/api-keys) 🇨🇦

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** —

A Cohere account automatically receives a trial API key. Trial API usage is free but limited.

**Quota:** The documented monthly trial limit is 1,000 calls; endpoint-specific limits also apply.

**Base URL:** `https://api.cohere.com/v2`

**Models:** `command-a-03-2025` (text); `command-a-vision-07-2025` (text, image); `embed-v4.0` (embedding); `rerank-v3.5` (reranking)

**Last verified:** 2026-09-20 · [official_docs sources](https://docs.cohere.com/docs/cohere-faqs)

### 🧪 [DeepSeek API](https://platform.deepseek.com/) 🇨🇳

**Access:** OmniRoute integration · **Card:** No · **OpenAI-compatible:** ✅

OmniRoute's current September 2026 catalog records a one-time free signup grant for the DeepSeek API.

**Quota:** Current catalog evidence records 5M free tokens on signup for a limited period; confirm current account eligibility before relying on it.

**Base URL:** `https://api.deepseek.com`

**Models:** `deepseek-chat` (text); `deepseek-reasoner` (text, reasoning)

**Last verified:** 2026-09-20 · [official_docs_plus_omniroute_audit sources](https://api-docs.deepseek.com/)

### 🧪 [Google Cloud Vertex AI](https://console.cloud.google.com/) 🇺🇸

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** —

New Google Cloud customers can receive $300 in free credits that may be used for eligible Vertex AI workloads.

**Quota:** $300 new-customer cloud credit; one-time trial rather than a permanent API quota.

**Base URL:** `https://aiplatform.googleapis.com`

**Models:** `gemini-flash-family` (text, image, audio, video); `gemma-family` (text)

**Last verified:** 2026-09-20 · [official_google_cloud_docs sources](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts)

### 🔄 [Google Gemini API](https://aistudio.google.com/app/apikey) 🇺🇸

**Access:** Login + API key · **Card:** No · **OpenAI-compatible:** ✅

New Gemini API accounts start on the Free Tier with access to selected models within their model-specific free-tier limits.

**Quota:** Model-specific quotas; current exact limits are shown in the account/AI Studio quota view.

**Base URL:** `https://generativelanguage.googleapis.com/v1beta`

**Models:** `gemini-2.5-flash` (text, image, audio, video); `gemini-2.5-flash-lite` (text, image, audio, video); `gemini-2.5-pro` (text, image, audio, video); `gemma-4-31b-it` (text)

**Last verified:** 2026-09-20 · [official_docs sources](https://ai.google.dev/gemini-api/docs/get-started)

### 🧪 [LongCat API](https://longcat.ai/platform/) 🇨🇳

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

OmniRoute's current free catalog records a one-time LongCat free allocation; the LongCat platform provides a first-party OpenAI-compatible API.

**Quota:** Current OmniRoute evidence records a one-time 10M-token free allocation; verify the live LongCat account quota before use.

**Base URL:** `https://api.longcat.chat/openai/v1`

**Models:** `LongCat-2.0` (text)

**Last verified:** 2026-09-20 · [official_longcat_docs_plus_omniroute_audit sources](https://longcat.ai/platform/docs/)

### 🔄 [Mistral AI](https://console.mistral.ai/api-keys) 🇫🇷

**Access:** Login + API key · **Card:** No · **OpenAI-compatible:** ✅

Mistral Studio starts in Free mode by default, with API access and limited included usage; no credit card is required to activate Studio.

**Quota:** Monthly included usage and limits are shown in the account Limits/Subscription views.

**Base URL:** `https://api.mistral.ai/v1`

**Models:** `mistral-small-latest` (text); `mistral-large-latest` (text); `codestral-latest` (text, code); `ministral-3-14b-latest` (text, image)

**Last verified:** 2026-09-20 · [official_docs sources](https://docs.mistral.ai/getting-started/quickstarts/developer/first-api-request)

### 🧪 [SEA-LION API](https://docs.sea-lion.ai/guides/inferencing/api) 🇸🇬

**Access:** OmniRoute integration · **Card:** No · **OpenAI-compatible:** ✅

AI Singapore provides a free SEA-LION API for proof-of-concept development and testing.

**Quota:** 10 requests/minute on the free API; intended for POC use rather than production workloads.

**Base URL:** `https://api.sea-lion.ai/v1`

**Models:** `aisingapore/Llama-SEA-LION-v3.5-70B-R` (text); `aisingapore/Qwen-SEA-LION-v4.5-27B-IT` (text)

**Last verified:** 2026-09-20 · [official_provider_docs sources](https://docs.sea-lion.ai/guides/inferencing/api)

### 🆓 [Z AI (Zhipu AI)](https://open.bigmodel.cn/usercenter/apikeys) 🇨🇳

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

Z AI publishes selected models at Free pricing, including GLM-4.7-Flash and other free variants.

**Quota:** Limits are model/account specific; published free models may be concurrency limited.

**Base URL:** `https://api.z.ai/api/paas/v4`

**Models:** `glm-4.7-flash` (text); `glm-4.5-flash` (text); `glm-4.6v-flash` (text, image)

**Last verified:** 2026-09-20 · [official_docs_and_provider_catalog sources](https://docs.z.ai/guides/develop/http/introduction)

## Inference providers and gateways

These platforms host or expose models from multiple sources.

### 🔑 [AI Horde](https://aihorde.net/register) 🌐

**Access:** OmniRoute integration · **Card:** No · **OpenAI-compatible:** —

AI Horde provides community-backed AI inference that is free of charge, with anonymous use supported.

**Quota:** Availability and speed depend on the community worker pool rather than a fixed commercial token quota.

**Base URL:** `https://aihorde.net/api/v2`

**Models:** `aphrodite/TheDrummer/Cydonia-24B-v4.3` (text); `aphrodite/TheDrummer/Skyfall-31B-v4.2` (text)

**Last verified:** 2026-09-20 · [official_site_plus_omniroute_audit sources](https://aihorde.net/api)

### 📅 [API Airforce](https://api.airforce/) 🌐

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

API Airforce documents a Free plan for API experimentation.

**Quota:** Published Free plan limit: 1 RPM and 1,000 requests/day.

**Base URL:** `https://api.airforce`

**Models:** `deepseek/deepseek-v3` (text); `qwen/qwen3-32b` (text); `google/gemini-2.5-flash` (text, image)

**Last verified:** 2026-09-20 · [official_docs sources](https://api.airforce/docs/quickstart/)

### 🆓 [BazaarLink](https://bazaarlink.ai/en/docs) 🌐

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

BazaarLink exposes an `auto:free` route and publishes a live set of free models.

**Quota:** Free routing is subject to the provider's current RPM/daily cap; the live /v1/models catalog marks free models with a :free suffix.

**Base URL:** `https://api.bazaarlink.ai/v1`

**Models:** `auto:free` (text); `claude-sonnet-4.6` (text); `gpt-5.4-mini` (text)

**Last verified:** 2026-09-20 · [official_docs_plus_omniroute_audit sources](https://bazaarlink.ai/en/docs)

### 📅 [Cloudflare Workers AI](https://dash.cloudflare.com/) 🇺🇸

**Access:** Login + token · **Card:** Unknown · **OpenAI-compatible:** ✅

Workers AI is available on Cloudflare's Free plan with 10,000 Neurons/day at no charge.

**Quota:** 10,000 Neurons/day shared across Workers AI usage; limits reset daily at 00:00 UTC.

**Base URL:** `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run`

**Models:** `@cf/meta/llama-3.3-70b-instruct-fp8-fast` (text); `@cf/meta/llama-4-scout-17b-16e-instruct` (text, image); `@cf/google/gemma-4-26b-a4b-it` (text, image); `@cf/openai/gpt-oss-120b` (text)

**Last verified:** 2026-09-20 · [official_docs sources](https://developers.cloudflare.com/workers-ai/get-started/rest-api/)

### 🔄 [Groq](https://console.groq.com/keys) 🇺🇸

**Access:** Login + API key · **Card:** No · **OpenAI-compatible:** ✅

Groq exposes a Free tier with model-specific request/token limits; payment information is needed only when upgrading to paid usage.

**Quota:** Limits are model and organization specific; the public rate-limit page lists current model ceilings and response headers expose remaining quota.

**Base URL:** `https://api.groq.com/openai/v1`

**Models:** `openai/gpt-oss-120b` (text — 30 RPM, 1,000 RPD; 8K TPM on the published table); `openai/gpt-oss-20b` (text — 30 RPM, 1,000 RPD; 8K TPM on the published table); `groq/compound` (text — 30 RPM, 250 RPD on the published table); `whisper-large-v3` (audio — 20 RPM, 2,000 RPD on the published table)

**Last verified:** 2026-09-20 · [official_docs sources](https://console.groq.com/docs/quickstart)

### 💵 [Hugging Face Inference Providers](https://huggingface.co/settings/tokens) 🇺🇸

**Access:** Login + token · **Card:** Unknown · **OpenAI-compatible:** ✅

Free Hugging Face users receive $0.10/month in Inference Provider credits, subject to change.

**Quota:** $0.10/month for Free users; additional usage requires purchased credits or another billing arrangement.

**Base URL:** `https://router.huggingface.co/v1`

**Models:** `meta-llama/Llama-3.1-8B-Instruct` (text); `google/gemma-3-4b-it` (text, image); `microsoft/phi-4` (text); `Qwen/Qwen2.5-Coder-7B-Instruct` (text, code)

**Last verified:** 2026-09-20 · [official_docs sources](https://huggingface.co/docs/inference-providers)

### 🧪 [Hyperbolic](https://app.hyperbolic.ai/) 🌐

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

OmniRoute's current catalog records a signup credit for Hyperbolic API experimentation.

**Quota:** Signup credit is one-time rather than a recurring free allowance; confirm the live account offer.

**Base URL:** `https://api.hyperbolic.xyz/v1`

**Models:** `qwen` (text); `llama` (text); `deepseek` (text, reasoning)

**Last verified:** 2026-09-20 · [omniroute_catalog_plus_official_docs sources](https://docs.hyperbolic.ai/)

### 🆓 [Kilo Code](https://app.kilo.ai/profile) 🇺🇸

**Access:** No login · **Card:** Unknown · **OpenAI-compatible:** ✅

Kilo Code exposes a free model pool, including an auto-router, with no API key required for the free gateway path.

**Quota:** Published free-gateway access is rate limited; the provider documents 200 requests/hour per IP for the free pool.

**Base URL:** `https://api.kilo.ai/api/gateway`

**Models:** `kilo-auto/free` (text); `nvidia/nemotron-3-ultra-550b-a55b:free` (text); `stepfun/step-3.7-flash:free` (text, image); `poolside/laguna-s-2.1:free` (text, code)

**Last verified:** 2026-09-20 · [provider_docs_and_live_reference sources](https://kilo.ai/docs/gateway/authentication)

### 🔄 [Kiro AI (OmniRoute upstream)](https://kiro.dev/) 🇺🇸

**Access:** OmniRoute integration · **Card:** No · **OpenAI-compatible:** —

OmniRoute documents Kiro AI as a free upstream connection with no API key required in the OmniRoute provider flow. Kiro itself has a perpetual Free tier with 50 credits/month; the upstream service terms govern access to the models.

**Quota:** Kiro Free currently lists 50 credits per monthly billing cycle; exact model/rate consumption depends on the request. OmniRoute may abstract provide…

**Endpoint:** `https://kiro.dev/`

**Models:** `Claude Sonnet 4.5` (text); `Qwen3 Coder Next` (text, code); `DeepSeek 3.2` (text, code)

**Last verified:** 2026-09-20 · [official_kiro_docs_and_omniroute_provider_guide sources](https://github.com/diegosouzapw/OmniRoute/wiki/Providers-Guide)

### 🔑 [LLM7.io](https://token.llm7.io) 🇬🇧

**Access:** No login · **Card:** No · **OpenAI-compatible:** ✅

LLM7 offers anonymous access to a free model pool; a free token raises the limits while keeping the same free models.

**Quota:** Anonymous: 10 RPM, 60 requests/hour and 500k tokens/day; free-token limits are higher according to the provider's limits page.

**Base URL:** `https://api.llm7.io/v1`

**Models:** `gpt-oss:20b` (text); `mistral-Nemo-Instruct-2407` (text); `minimax-m2.7` (text)

**Last verified:** 2026-09-20 · [provider_docs_and_live_reference sources](https://docs.llm7.io/)

### 🔄 [ModelScope API-Inference](https://modelscope.cn/my/myaccesstoken) 🇨🇳

**Access:** Login + token · **Card:** Unknown · **OpenAI-compatible:** ✅

ModelScope provides free API-Inference for registered users under published usage/concurrency limits.

**Quota:** Published limits include 2,000 requests/day total per user, with per-model quotas dynamically adjusted and capped at 500.

**Base URL:** `https://api-inference.modelscope.cn/v1`

**Models:** `Qwen/Qwen3.5-35B-A3B` (text); `Qwen/Qwen3.5-27B` (text); `Qwen/Qwen3.6-35B-A3B` (text)

**Last verified:** 2026-09-20 · [provider_docs sources](https://modelscope.cn/docs/model-service/API-Inference/intro)

### 💵 [Morph](https://www.morphllm.com/) 🇺🇸

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

Morph publishes an OpenAI-compatible API with 200 free requests every month.

**Quota:** 200 requests/month free; hosted model usage after the free allowance is usage-priced.

**Base URL:** `https://api.morphllm.com/v1`

**Models:** `morph-kimik3` (text, image); `morph-glm53flash` (text); `morph-dsv41flash` (text)

**Last verified:** 2026-09-20 · [official_morph_pricing_and_models sources](https://www.morphllm.com/models)

### 📅 [Nara Router](https://router.bynara.id/) 🇮🇩

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

Nara currently publishes a Free plan with a daily token allowance and no paid subscription required for the free path.

**Quota:** 7M tokens/day and 15 RPM on the currently published Free plan; the daily pool is shared across its free models.

**Base URL:** `https://router.bynara.id/api`

**Models:** `agnes-2.0-flash` (text); `laguna-s-2.1` (text); `mistral-large` (text); `qwen3.8-27b` (text)

**Last verified:** 2026-09-20 · [official_provider_page_plus_omniroute_audit sources](https://router.bynara.id/docs)

### 📅 [NavyAI](https://api.navy/) 🌐

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

NavyAI currently advertises a $0 Free plan for API use.

**Quota:** The current public plan page advertises 150K tokens/day and 20 RPM.

**Base URL:** `https://api.navy/v1`

**Models:** `shared-free-pool` (text)

**Last verified:** 2026-09-20 · [official_provider_page_plus_omniroute_audit sources](https://api.navy/)

### 🔄 [NVIDIA NIM](https://build.nvidia.com/explore/discover) 🇺🇸

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

NVIDIA NIM provides API access to selected models for NVIDIA Developer Program members, subject to model-specific limits.

**Quota:** The reference snapshot lists 40 RPM and 10,000 requests/day for its included models; check the current NVIDIA model page for live limits.

**Base URL:** `https://integrate.api.nvidia.com/v1`

**Models:** `nvidia/nemotron-3-super-120b-a12b` (text — 40 RPM, 10,000 RPD (reference snapshot)); `nvidia/nemotron-3-nano-30b-a3b` (text — 40 RPM, 10,000 RPD (reference snapshot)); `meta/llama-3.3-70b-instruct` (text — 40 RPM, 10,000 RPD (reference snapshot)); `openai/gpt-oss-120b` (text — 40 RPM, 10,000 RPD (reference snapshot))

**Last verified:** 2026-09-20 · [official_nvidia_docs_plus_reference_crosscheck sources](https://docs.api.nvidia.com/nim/)

### 🔄 [Ollama Cloud](https://ollama.com/settings/keys) 🇺🇸

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

Ollama Cloud provides a free tier with session and weekly usage limits for supported cloud model families.

**Quota:** Session limits reset every five hours and weekly limits reset every seven days; exact model weighting varies.

**Base URL:** `https://ollama.com/api`

**Models:** `deepseek-v4-pro` (text); `deepseek-v4-flash` (text); `minimax-m3` (text); `gpt-oss:120b` (text)

**Last verified:** 2026-09-20 · [provider_docs sources](https://docs.ollama.com/cloud)

### 🆓 [OpenCode Free (OmniRoute upstream)](https://opencode.ai/) 🇺🇸

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

OmniRoute documents an OpenCode Free upstream with no API key required in its provider flow. OpenCode’s own Zen documentation currently describes several free models as available for a limited time, so this entry is not classified as a permanent free tier.

**Quota:** Free-model availability and limits are model-specific and can change; current OpenCode documentation lists free models such as MiMo-V2.5 Free, Ling…

**Base URL:** `https://opencode.ai/zen/v1`

**Models:** `mimo-v2.5-free` (text); `ling-3.0-flash-fin-free` (text); `nemotron-3-ultra-free` (text, code); `nemotron-3.5-lightning-free` (text, code); `big-pickle` (text, code)

**Last verified:** 2026-09-20 · [official_opencode_docs_and_omniroute_provider_guide sources](https://opencode.ai/docs/zen)

### 🆓 [OpenRouter](https://openrouter.ai/keys) 🇺🇸

**Access:** Login + API key · **Card:** No · **OpenAI-compatible:** ✅

OpenRouter's Free plan provides API access to 25+ free models and currently lists a 50 requests/day rate limit.

**Quota:** 50 requests/day on the Free plan; free model availability changes frequently.

**Base URL:** `https://openrouter.ai/api/v1`

**Models:** `openrouter/free` (text, image — 50 RPD on Free plan); `nvidia/nemotron-3-super-120b-a12b:free` (text); `openai/gpt-oss-20b:free` (text); `google/gemma-4-31b-it:free` (text, image)

**Last verified:** 2026-09-20 · [official_docs sources](https://openrouter.ai/docs)

### 👤 [OVHcloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) 🇫🇷

**Access:** No login · **Card:** No · **OpenAI-compatible:** ✅

OVHcloud AI Endpoints currently offers a free anonymous tier without signup or API key at a low per-IP/per-model rate.

**Quota:** 2 requests/minute per IP per model on the anonymous free path; higher limits are paid.

**Base URL:** `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`

**Models:** `Qwen3.5-397B-A17B` (text); `gpt-oss-120b` (text); `Meta-Llama-3_3-70B-Instruct` (text); `Qwen2.5-VL-72B-Instruct` (text, image)

**Last verified:** 2026-09-20 · [reference_repo_and_provider_catalog sources](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/)

### 🔑 [Pollinations (OmniRoute upstream)](https://pollinations.ai/) 🇩🇪

**Access:** OmniRoute integration · **Card:** Unknown · **OpenAI-compatible:** ✅

OmniRoute documents Pollinations as a no-key free upstream. Pollinations also maintains an OpenAI-compatible API and multiple access levels; direct API limits and authentication options should be checked against its current API documentation.

**Quota:** No single stable quota is asserted here because Pollinations exposes different free/registered/key-based access paths and model-specific rules; use…

**Base URL:** `https://gen.pollinations.ai/v1`

**Models:** `openai/gpt-5.4-nano` (text); `openai/gpt-oss-20b` (text); `anthropic/claude-sonnet-4.6` (text); `google/gemini-3.7-flash` (text, image); `deepseek/deepseek-v4-flash` (text)

**Last verified:** 2026-09-20 · [official_pollinations_docs_and_omniroute_provider_guide sources](https://github.com/pollinations/pollinations/blob/main/APIDOCS.md)

### 🔄 [Public AI Gateway](https://platform.publicai.co/) 🌐

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

Public AI documents a Free tier with API access to public and sovereign models.

**Quota:** The current Free tier is documented at 100 requests/minute; paid/Plus plans increase that limit.

**Base URL:** `https://api.publicai.co/v1`

**Models:** `swiss-ai/apertus-v1.5-8b` (text); `aisingapore/sea-lion` (text)

**Last verified:** 2026-09-20 · [official_publicai_docs sources](https://platform.publicai.co/docs)

### 🆓 [SiliconFlow](https://cloud.siliconflow.cn/account/ak) 🇨🇳

**Access:** Login + API key · **Card:** Unknown · **OpenAI-compatible:** ✅

SiliconFlow has model-specific free models whose calls are priced at zero after the account requirements are satisfied.

**Quota:** Free-model rate limits are fixed per model; exact limits are exposed by the model catalog.

**Base URL:** `https://api.siliconflow.cn/v1`

**Models:** `Qwen/Qwen3-8B` (text); `Hunyuan-MT-7B` (text); `Qwen3.5-4B` (text); `THUDM/GLM-4-9B-0414` (text)

**Last verified:** 2026-09-20 · [provider_docs sources](https://api-docs.siliconflow.cn/)

### 📅 [xKiro](https://xkiro.com/) 🌐

**Access:** OmniRoute integration · **Card:** No · **OpenAI-compatible:** ✅

xKiro documents a Free plan with access to free-tier models on free accounts.

**Quota:** The current documentation exposes a daily account-level free-token allowance; exact limits are returned by the live usage endpoint.

**Base URL:** `https://api.xkiro.com/v1`

**Models:** `qwen/qwen3.5-flash:free` (text, image); `minimax/minimax-m2.7:free` (text); `mistralai/mistral-small-2603` (text)

**Last verified:** 2026-09-20 · [official_xkiro_docs_plus_omniroute_audit sources](https://docs.xkiro.com/guides/pricing/)

## Gateways and routers

Self-hosted or routing layers are listed separately from direct model providers. Their free capacity depends on the upstream providers you connect; they are not counted as an independent free-token pool.

### 🧭 [OmniRoute](https://github.com/diegosouzapw/OmniRoute) 🇧🇷

**Access:** No OmniRoute account · **Card:** No · **OpenAI-compatible:** ✅

OmniRoute is a free MIT-licensed self-hosted AI gateway. It does not provide a single hosted free quota; instead, it lets you connect free providers and route requests through one local OpenAI-compatible endpoint.

**Quota:** No separate OmniRoute quota. Available capacity follows the free or paid quotas of the providers you connect; documented routing supports automatic…

**Base URL:** `http://localhost:20128/v1`

**Routes:** `auto` (text, multimodal); `auto/coding` (text, code); `auto/fast` (text, multimodal); `auto/cheap` (text, multimodal); `auto/offline` (text, multimodal); `auto/smart` (text, multimodal)
**Default route:** `auto`

**Route guide:** `auto` — Balanced default: automatic selection among connected providers.; `auto/coding` — Use for coding and software-engineering tasks.; `auto/fast` — Use when latency is the primary objective.; `auto/cheap` — Use when minimizing cost is the primary objective.; `auto/offline` — Use when maximizing quota/availability headroom is the priority.; `auto/smart` — Use when prioritizing quality while allowing exploration.

**Last verified:** 2026-09-20 · [official_repo_and_docs sources](https://github.com/diegosouzapw/OmniRoute/wiki/Quick-Start)

## OmniRoute upstreams

These are provider integrations that OmniRoute documents as free upstream paths. They are listed separately so the atlas does not imply that OmniRoute itself creates provider quota or that the upstream's direct API terms are identical to its OmniRoute adapter path.

| Upstream | OmniRoute access | Free classification | Direct API note |
|---|---|---|---|
| [Kiro AI (OmniRoute upstream)](https://kiro.dev/) | ✅ | 🔄 recurring_free_tier | not_catalogued_as_standalone_public_api_here |
| [OpenCode Free (OmniRoute upstream)](https://opencode.ai/) | ✅ | 🆓 free_models | authenticated_direct_access_documented_separately |
| [Pollinations (OmniRoute upstream)](https://pollinations.ai/) | ✅ | 🔑 keyless_or_free_token | openai_compatible_api_documented |
| [Nara Router](https://router.bynara.id/) | ✅ | 📅 daily_free_allocation | see provider docs |
| [xKiro](https://xkiro.com/) | ✅ | 📅 daily_free_allocation | Direct API documented; free models are subject to account-level allowance. |
| [API Airforce](https://api.airforce/) | ✅ | 📅 daily_free_allocation | see provider docs |
| [BazaarLink](https://bazaarlink.ai/en/docs) | ✅ | 🆓 free_pool | see provider docs |
| [NavyAI](https://api.navy/) | ✅ | 📅 daily_free_allocation | see provider docs |
| [AI Horde](https://aihorde.net/register) | ✅ | 🔑 keyless_or_free_token | Native Horde API; not an OpenAI-compatible direct endpoint. |
| [SEA-LION API](https://docs.sea-lion.ai/guides/inferencing/api) | ✅ | 🧪 free_trial_key | see provider docs |
| [Baidu Qianfan ERNIE](https://console.bce.baidu.com/qianfan/ais/console/apiKey) | ✅ | ♾️ permanent_free_tier | see provider docs |
| [DeepSeek API](https://platform.deepseek.com/) | ✅ | 🧪 free_trial_key | see provider docs |
| [Google Cloud Vertex AI](https://console.cloud.google.com/) | ✅ | 🧪 free_trial_key | see provider docs |
| [Hyperbolic](https://app.hyperbolic.ai/) | ✅ | 🧪 free_trial_key | see provider docs |
| [LongCat API](https://longcat.ai/platform/) | ✅ | 🧪 free_trial_key | see provider docs |
## OmniRoute free catalog

OmniRoute's current free-tier catalog is tracked as a discovery snapshot. These provider IDs are not automatically promoted to detailed direct-API records; some are adapters, web tools, trials, regional offers, or terms-sensitive proxy paths.

**78 OmniRoute catalog provider IDs** · source: [https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/FREE_TIERS.md](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/FREE_TIERS.md)

| OmniRoute provider | Free classification | Terms flag | Note |
|---|---|---|---|
| agentrouter | signup_credit | caution |  |
| agnes | uncapped | ok |  |
| agnes-cn | uncapped | ok |  |
| agy | keyless | avoid |  |
| ai21 | signup_credit | avoid |  |
| aihorde | keyless | ok |  |
| ainative | uncapped | caution |  |
| aion | uncapped | ok |  |
| api-airforce | recurring | caution |  |
| arcee-ai | recurring | caution |  |
| baichuan | signup_credit | ambiguous |  |
| baidu | uncapped | caution |  |
| bazaarlink | recurring | caution |  |
| blackbox | keyless | avoid |  |
| bluesminds | recurring | ambiguous |  |
| bytez | recurring | ambiguous |  |
| cerebras | signup_credit | caution |  |
| cloudflare-ai | recurring | caution |  |
| cohere | one_time | caution |  |
| coze | recurring | avoid |  |
| deepinfra | signup_credit | caution |  |
| deepseek | signup_credit | ok |  |
| doubao | signup_credit | ambiguous |  |
| duckduckgo-web | keyless | avoid |  |
| fireworks | signup_credit | avoid |  |
| freemodel-dev | signup_credit | unknown |  |
| friendliai | keyless | avoid |  |
| gemini | uncapped | caution |  |
| glm | uncapped | ok |  |
| glm-cn | uncapped | ok |  |
| groq | recurring | caution |  |
| huggingchat | one_time | caution |  |
| huggingface | one_time | caution |  |
| hyperbolic | signup_credit | ok |  |
| iflytek | keyless | avoid |  |
| inference-net | one_time | caution |  |
| kilo-gateway | uncapped | caution |  |
| kiro | one_time | avoid |  |
| liquid | keyless | unknown |  |
| llm7 | recurring | caution |  |
| longcat | signup_credit | caution |  |
| mistral | one_time | caution |  |
| modelscope | recurring | caution |  |
| monsterapi | signup_credit | ambiguous |  |
| morph | one_time | ok |  |
| muse-spark-web | keyless | avoid |  |
| nara | recurring | caution |  |
| navy | recurring | ok |  |
| nebius | signup_credit | caution |  |
| nlpcloud | one_time | avoid |  |
| nous-research | recurring | ambiguous |  |
| novita | signup_credit | caution |  |
| nscale | signup_credit | caution |  |
| nvidia | signup_credit | caution |  |
| ollama-cloud | uncapped | ambiguous |  |
| opencode | keyless | avoid |  |
| opencode-zen | uncapped | caution |  |
| openrouter | recurring | caution |  |
| ovhcloud | keyless | ok |  |
| pollinations | keyless | caution |  |
| predibase | signup_credit | caution |  |
| publicai | signup_credit | caution |  |
| qoder | signup_credit | caution |  |
| reka | one_time | caution |  |
| requesty | uncapped | ok |  |
| routeway | uncapped | caution |  |
| sambanova | recurring | caution |  |
| scaleway | signup_credit | ok |  |
| sealion | uncapped | ok |  |
| sensenova | signup_credit | caution |  |
| siliconflow | uncapped | caution |  |
| sparkdesk | keyless | caution |  |
| stepfun | signup_credit | ok |  |
| t3-web | recurring | avoid |  |
| tencent | uncapped | caution |  |
| uncloseai | keyless | caution |  |
| vertex | signup_credit | caution |  |
| xkiro | recurring | caution |  |

## Google Antigravity free models

Google Antigravity currently lists these models as available on the **$0/month Individual plan**. This is a product-access catalog, not a standalone public inference-API claim.

| Model | Provider | Type | Free access | Notes |
|---|---|---|---|---|
| gemini-3.8-flash | Google | reasoning | ✅ Individual | Selectable reasoning model. |
| gemini-3.7-flash | Google | reasoning | ✅ Individual | Selectable reasoning model. |
| gemini-3.6-flash | Google | reasoning | ✅ Individual | Selectable reasoning model. |
| gemini-3.1-pro | Google | reasoning | ✅ Individual | Selectable reasoning model. |
| claude-sonnet-4.6 | Anthropic | reasoning | ✅ Individual | Selectable reasoning model; thinking mode. |
| claude-opus-4.6 | Anthropic | reasoning | ✅ Individual | Selectable reasoning model; thinking mode. |
| gpt-oss-120b | OpenAI | reasoning | ✅ Individual | Selectable reasoning model. |

**Additional product models:** nano-banana-2 (Google; internal_product_use)

**Usage:** Free users receive meaningful baseline quota refreshed weekly, with weekly rate limits. Exact usage limits are dynamic and are shown in the Antigravity model/usage UI. Availability and limits can change with capacity and service updates. The product supports desktop access on Windows, macOS, and Linux.

**Sources:** [https://antigravity.google/docs/models/](https://antigravity.google/docs/models/); [https://antigravity.google/docs/plans](https://antigravity.google/docs/plans); [https://antigravity.google/pricing](https://antigravity.google/pricing)

## OmniRoute model-level free catalog

The imported OmniRoute **release/v3.8.51** snapshot contains **489 free-model catalog records**, including **482 non-discontinued records** and **7 records marked discontinued** in the source. It covers **78 provider IDs** and **77 pool keys**.

These are **access-path records**, not 489 unique underlying models: the same model can appear through multiple providers or shared pools. The full machine-readable snapshot preserves the provider, exact model ID, free-access classification, pool key, ToS flag, and token/credit fields.

Full snapshot: [data/omniroute-free-models.json](data/omniroute-free-models.json).

## Verification model

Every provider entry has a `last_verified` date and one or more source URLs. Free access is classified so a $0 recurring quota is not silently presented as the same thing as a time-limited promotion or a small trial credit.

### Status meanings

| Field | Meaning |
|---|---|
| `permanent_free_tier` | Provider describes an ongoing free tier |
| `recurring_free_tier` | Free allocation renews on a recurring basis |
| `free_models` | Specific models are priced at $0 |
| `free_trial_key` | Account receives a free but limited trial key |
| `monthly_credit` | Free account receives a recurring credit allocation |
| `daily_free_allocation` | Free allocation resets daily |
| `free_pool` | Provider maintains a free model pool/router |
| `keyless_or_free_token` | Anonymous access and/or a free token exists |
| `anonymous_free_tier` | Free anonymous API path exists |
| `self_hosted_free_gateway` | Self-hosted gateway whose free capacity comes from connected upstream providers |

## 🧯 Stale-data defense

This project also records notable provider retirements so older tutorials and lists can be checked against a maintained record.

| Service | Retired | Evidence |
|---|---|---|
| GitHub Models | 2026-07-30 | [Provider notice](https://docs.github.com/en/github-models) |

## ⚠️ Important

Free AI APIs change quickly. Model catalogs, quotas, account requirements, regional availability, and data-use terms can change without notice. Always open the linked provider documentation before using an API in production or sending confidential data.

This project does not store API keys and never asks contributors to submit secrets. Verification workflows should use repository secrets or public metadata only.

## Contributing

Add the provider to `data/providers.json`, include primary evidence, and let CI validate the structure. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
