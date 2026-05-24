<div align="center">

# 📖 MiMoReadme

**AI-Powered README Generator — Powered by Xiaomi MiMo V2.5**

[![Made with MiMo](https://img.shields.io/badge/Made_with-Xiaomi_MiMo_V2.5-ff6900?style=for-the-badge)](https://mimo.money)
[![GitHub Pages](https://img.shields.io/badge/Live-GitHub_Pages-222?style=for-the-badge&logo=github)](https://gyoomei.github.io/mimoreadme/)
[![Zero Backend](https://img.shields.io/badge/Backend-Zero-10b981?style=for-the-badge)](#)
[![Single HTML](https://img.shields.io/badge/File-Single_HTML-6366f1?style=for-the-badge)](#)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=flat-square)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000&style=flat-square)](#)
[![MiMo AI](https://img.shields.io/badge/AI-Xiaomi_MiMo_V2.5-ff6900?style=flat-square)](#)
[![Pollinations](https://img.shields.io/badge/API-Pollinations.ai-green?style=flat-square)](#)

</div>

---

**MiMoReadme** generates production-ready README.md files from a GitHub URL or manual input. Pick a template, toggle sections, hit generate — your README appears in seconds with live preview, badge generation, and MiMo-powered chat refinement.

## The Problem

Writing a good README takes 30-60 minutes. You research badge syntax, format sections, write install steps, hunt for shields.io URLs. Most devs either skip it (empty repos) or copy-paste generic templates that don't fit their project.

## How It Works

1. **Paste** your GitHub repo URL or fill in project details manually
2. **Pick** a template: Modern, Classic, Minimal, Hackathon, or MiMo 100T
3. **Toggle** sections on/off: Badges, Features, Demo, Installation, Usage, Tech Stack, API, Contributing, License, Screenshots, Roadmap
4. **Generate** — MiMo V2.5 writes the entire README in seconds
5. **Refine** via the built-in chat widget — ask MiMo to fix wording, add sections, suggest badges
6. **Export** — copy to clipboard or download README.md

That's the entire UX. No signup, no API key, no backend.

## Features

- **5 README Templates** — Modern (badges + clean), Classic (traditional dev), Minimal (bare essentials), Hackathon (DevPost ready), MiMo 100T (shields.io hero + narrative structure)
- **12 Toggleable Sections** — Enable only what you need: Badges, Features, Demo, Installation, Usage, Tech Stack, API, Contributing, License, Acknowledgments, Screenshots, Roadmap
- **Live Preview** — Side-by-side markdown editor and rendered preview (tabbed on mobile)
- **Chat with MiMo** — Built-in AI widget to refine, expand, or rewrite sections conversationally
- **Badge Generator** — shields.io integration with live preview for tech, license, and status badges
- **GitHub URL Auto-Fill** — Paste a repo URL, project name and structure extracted automatically
- **Dark/Light Theme** — CSS variable system with animated mesh gradient, floating particles, glassmorphism borders
- **Zero Dependencies** — Single HTML file, no build step, no npm, no backend
- **Fully Responsive** — Works on 375px phones to 1440px desktops

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   index.html                     │
│  ┌───────────┐  ┌───────────┐  ┌─────────────┐  │
│  │  Input UI  │  │ Template  │  │  Section    │  │
│  │ (URL/manual│  │ Selector  │  │  Toggles    │  │
│  └─────┬─────┘  └─────┬─────┘  └──────┬──────┘  │
│        │              │               │          │
│        ▼              ▼               ▼          │
│  ┌──────────────────────────────────────────┐    │
│  │          Prompt Builder                  │    │
│  └──────────────────┬───────────────────────┘    │
│                     │                            │
│                     ▼                            │
│  ┌──────────────────────────────────────────┐    │
│  │  Pollinations.ai → MiMo V2.5             │    │
│  │  POST /openai  model=openai              │    │
│  └──────────────────┬───────────────────────┘    │
│                     │                            │
│        ┌────────────┴────────────┐               │
│        ▼                        ▼               │
│  ┌───────────┐          ┌───────────┐           │
│  │ Raw Editor │          │ Rendered  │           │
│  │ (markdown) │          │ Preview   │           │
│  └───────────┘          └───────────┘           │
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │  Chat Widget → MiMo V2.5                 │    │
│  │  Conversational README refinement        │    │
│  └──────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

## Performance

| Metric | Value |
|--------|-------|
| File size | 31 KB (single HTML) |
| Time to first README | ~5 seconds |
| Templates | 5 |
| Toggleable sections | 12 |
| External dependencies | 0 (CDN only) |
| Backend required | None |
| API keys needed | None |

## Security

- **No data storage** — Everything runs client-side, nothing is logged or stored server-side
- **No API keys** — Uses Pollinations.ai free tier, no secrets to manage
- **No cookies** — No tracking, no analytics, no third-party scripts beyond CDN
- **CSP-safe** — No eval, no inline event handlers (onclick used for simplicity, replaceable with addEventListener)
- **MiMo API** — Text-only via Pollinations.ai, no code execution, no file access

## What's Different

| Tool | Backend | API Key | Templates | AI Chat | Free |
|------|---------|---------|-----------|---------|------|
| **MiMoReadme** | None | None | 5 | ✅ MiMo | ✅ |
| readme.so | None | None | 3 | ❌ | ✅ |
| readme.ai | ✅ | ✅ OpenAI | 1 | ✅ GPT | ❌ |
| GitHub Copilot | ✅ | ✅ GH Token | 1 | ✅ GPT-4 | ❌ |
| Markdown Badges | None | None | 0 | ❌ | ✅ |

MiMoReadme is the only tool that combines template variety, section toggles, live preview, AND free AI chat — all in a single zero-backend HTML file.

## Getting Started

### Use Online

Visit: **[gyoomei.github.io/mimoreadme](https://gyoomei.github.io/mimoreadme/)**

### Run Locally

```bash
git clone https://github.com/gyoomei/mimoreadme.git
cd mimoreadme
open index.html
# or
python3 -m http.server 8080
# → http://localhost:8080
```

No install, no build, no dependencies.

## Contributing

Contributions welcome! This is a single-file project — edit `index.html` directly.

1. Fork the repo
2. Make your changes
3. Test locally
4. Submit a PR

## License

MIT

---

<div align="center">

**Built for the [Xiaomi MiMo 100T Creator Program](https://mimo.money)**

</div>
