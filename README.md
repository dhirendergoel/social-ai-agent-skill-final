# 🤖 Social AI Agent Skill

> **A universal AI skill** that runs on Claude, Gemini, Grok, GPT-4, and any LLM — automating your entire social media presence across **Meta (Facebook, Instagram, Threads)**, **X (Twitter)**, **TikTok**, **LinkedIn**, **YouTube**, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Universal](https://img.shields.io/badge/Platform-Universal%20AI-blue.svg)]()
[![Platforms: Meta | X | TikTok](https://img.shields.io/badge/Social-Meta%20%7C%20X%20%7C%20TikTok%20%7C%20LinkedIn-brightgreen.svg)]()

---

## 🌟 What This Skill Does

This skill deploys a **multi-agent AI system** that fully automates social media marketing operations:

| Agent | Responsibility |
|-------|---------------|
| 🔬 **Research Agent** | Trend analysis, competitor research, audience insights |
| ✍️ **Content Agent** | Viral post copy, captions, long-form articles |
| 🎨 **Creative Agent** | Image prompts, visual design briefs, Reel/TikTok scripts |
| 🏷️ **Hashtag & Tagline Agent** | Platform-optimized hashtags, compelling CTAs |
| 📅 **Scheduler Agent** | Smart scheduling across time zones and peak times |
| 📢 **Publisher Agent** | Cross-platform publishing via APIs |
| 📊 **Analytics Agent** | Performance tracking, A/B testing suggestions |

---

## 📁 Repository Structure

```
social-ai-agent-skill/
├── SKILL.md                    # Main skill instruction file (all AI platforms)
├── README.md                   # This file
├── agents/
│   ├── research_agent.md       # Research & trend analysis agent
│   ├── content_agent.md        # Viral content creation agent
│   ├── creative_agent.md       # Visual & reel design agent
│   ├── hashtag_agent.md        # Hashtag & tagline agent
│   ├── scheduler_agent.md      # Smart scheduling agent
│   ├── publisher_agent.md      # Cross-platform publisher agent
│   └── analytics_agent.md     # Analytics & insights agent
├── platforms/
│   ├── meta.md                 # Meta (Facebook, Instagram, Threads) guide
│   ├── x_twitter.md            # X (Twitter) guide
│   ├── tiktok.md               # TikTok guide
│   ├── linkedin.md             # LinkedIn guide
│   └── youtube.md              # YouTube Shorts guide
├── content/
│   ├── viral_formulas.md       # Proven viral content formulas
│   ├── reel_scripts.md         # Reel / Short-form video scripts
│   ├── caption_templates.md    # Caption templates by niche
│   └── content_calendar.md    # Content calendar framework
├── tools/
│   ├── api_connector.py        # Unified social API connector
│   ├── content_generator.py    # AI content generation pipeline
│   ├── scheduler.py            # Content scheduling tool
│   ├── publisher.py            # Multi-platform publisher
│   └── analytics.py            # Analytics aggregator
├── configs/
│   ├── platforms.yaml          # Platform API configuration
│   ├── agents.yaml             # Agent orchestration config
│   └── content_rules.yaml      # Content guidelines & brand voice
├── examples/
│   ├── brand_launch.md         # Example: Brand launch campaign
│   ├── product_promo.md        # Example: Product promotion
│   └── daily_automation.md    # Example: Daily content automation
├── tests/
│   ├── test_agents.py          # Agent unit tests
│   └── test_publishers.py      # Publisher integration tests
├── docs/
│   ├── setup_guide.md          # Complete setup guide
│   ├── api_credentials.md      # API credentials guide
│   └── customization.md        # Customization guide
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions CI
```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/social-ai-agent-skill.git
cd social-ai-agent-skill
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API credentials
```bash
cp configs/platforms.yaml.example configs/platforms.yaml
# Edit configs/platforms.yaml with your API keys
```

### 4. Load the skill in your AI platform

**Claude (via CLAUDE.md or system prompt):**
```
Load the skill from SKILL.md and follow all instructions.
```

**Gemini / Antigravity:**
Place `SKILL.md` in your skills directory or reference it in your skill configuration.

**ChatGPT / GPT-4:**
Paste the contents of `SKILL.md` as a system message or Custom Instruction.

**Grok:**
Use `SKILL.md` as a system prompt in the API or xAI console.

---

## 🔑 Required API Credentials

| Platform | Required Keys |
|----------|--------------|
| Meta (Facebook/Instagram) | `META_APP_ID`, `META_APP_SECRET`, `ACCESS_TOKEN` |
| X (Twitter) | `API_KEY`, `API_SECRET`, `ACCESS_TOKEN`, `ACCESS_SECRET` |
| TikTok | `TIKTOK_CLIENT_KEY`, `TIKTOK_CLIENT_SECRET` |
| LinkedIn | `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET` |
| YouTube | `YOUTUBE_API_KEY`, `GOOGLE_OAUTH_CREDENTIALS` |
| AI Image Gen | `OPENAI_API_KEY` or `STABILITY_API_KEY` or `GEMINI_API_KEY` |

See [`docs/api_credentials.md`](docs/api_credentials.md) for step-by-step instructions.

---

## 🤖 Supported AI Platforms

| AI Platform | Integration Method | Status |
|-------------|-------------------|--------|
| **Claude** (Anthropic) | `CLAUDE.md` / System Prompt | ✅ Full |
| **Gemini** (Google) | Antigravity Skill / System Prompt | ✅ Full |
| **ChatGPT / GPT-4o** (OpenAI) | Custom Instructions / System Prompt | ✅ Full |
| **Grok** (xAI) | System Prompt | ✅ Full |
| **Llama 3** (Meta) | System Prompt | ✅ Full |
| **Mistral** | System Prompt | ✅ Full |
| **Copilot** (Microsoft) | System Prompt | ✅ Full |

---

## 📋 Usage Examples

### Launch a full campaign
```
Skill: social-ai-agent-skill
Task: Launch a campaign for [PRODUCT] targeting [AUDIENCE] on Instagram, X, and TikTok.
Brand voice: [casual/professional/humorous]
Budget for ads: [optional]
```

### Daily content automation
```
Skill: social-ai-agent-skill
Task: Create and schedule today's content for all platforms.
Niche: [your niche]
Posting frequency: 3x per day
```

### Viral reel creation
```
Skill: social-ai-agent-skill
Task: Create 5 viral reel scripts on the topic of [TOPIC].
Style: Educational + Entertainment
Duration: 30-60 seconds
```

---

## 🔧 Configuration

Edit [`configs/agents.yaml`](configs/agents.yaml) to customize agent behavior, model selection, and orchestration order.

Edit [`configs/content_rules.yaml`](configs/content_rules.yaml) to define:
- Brand voice and tone
- Prohibited topics
- Target audience
- Posting schedules

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Pull requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

---

## ⭐ Star this repo if it helps you!
