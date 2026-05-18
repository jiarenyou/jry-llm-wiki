#!/usr/bin/env python3
"""sync-root-index.py — Regenerate root index.md from wiki/overview.md.

Reads wiki/overview.md and wiki/index.md, then regenerates the content
sections of the root index.md. Manual sections (intro, quotes, footer)
are preserved via HTML comment markers.

Usage:
    python tools/sync-root-index.py          # regenerate index.md
    python tools/sync-root-index.py --check  # report differences only
    python tools/sync-root-index.py --init   # extract manual blocks from backup
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = REPO_ROOT / "index.md"
OVERVIEW_FILE = REPO_ROOT / "wiki" / "overview.md"

# ── helpers ──────────────────────────────────────────────────────────

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")

def extract_section(text: str, heading: str, level: int = 2) -> str | None:
    """Extract body text under a ##/### heading until next ## or end."""
    prefix = "#" * level
    pattern = rf'^{prefix} {re.escape(heading)}\s*\n(.*?)(?=^{prefix} |^## |\Z)'
    m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else None

def extract_all_h2_sections(text: str) -> dict[str, str]:
    """Return {heading_name: body_text} for all ## sections."""
    sections = {}
    for m in re.finditer(r'^## (.+?)\s*\n(.*?)(?=^## |\Z)', text, re.MULTILINE | re.DOTALL):
        sections[m.group(1).strip()] = m.group(2).strip()
    return sections

# ── content generators ───────────────────────────────────────────────

def gen_tech_section(overview_sections: dict[str, str]) -> str:
    """Generate 技术探索 section from LLM/AI + Big Data overview content."""
    lines = ['### 技术探索', '',
             '> [!tip|label:🔧 技术探索] 从 Transformer 到 Spark，从理论到工程']

    llm = overview_sections.get('一、LLM 与 AI 技术', '')
    bigdata = overview_sections.get('二、大数据工程与数仓', '')

    if llm:
        lines.append('>')
        lines.append('> **LLM & AI**')
        wikilinks = re.findall(r'\[\[(.+?)\]\]', llm)
        seen = set()
        for wl in wikilinks:
            if wl not in seen and wl:
                seen.add(wl)
            if len(seen) >= 4:
                break
        for wl in sorted(seen):
            lines.append(f'> - [[{wl}]]')

    if bigdata:
        lines.append('>')
        lines.append('> **大数据工程**')
        wikilinks = re.findall(r'\[\[(.+?)\]\]', bigdata)
        seen = set()
        for wl in wikilinks:
            if wl not in seen and wl:
                seen.add(wl)
            if len(seen) >= 3:
                break
        for wl in sorted(seen):
            lines.append(f'> - [[{wl}]]')

    lines.append('')
    return '\n'.join(lines)


def gen_philosophy_section(overview_sections: dict[str, str]) -> str:
    """Generate 哲学思辨 section."""
    lines = ['### 哲学思辨', '',
             '> [!note|label:💡 哲学思辨] 在东西方智慧之间寻找平衡']

    philo = overview_sections.get('四、哲学、经济学与文化', '')
    if philo:
        # Philosophy
        philo_sub = extract_section(philo, '哲学主线：认知边界与存在追问', level=3)
        philo_wl = set()
        if philo_sub:
            for wl in re.findall(r'\[\[(.+?)\]\]', philo_sub):
                if wl:
                    philo_wl.add(wl)

        # Economics
        econ_sub = extract_section(philo, '经济学主线：资源配置与博弈', level=3)
        econ_wl = set()
        if econ_sub:
            for wl in re.findall(r'\[\[(.+?)\]\]', econ_sub):
                if wl:
                    econ_wl.add(wl)

        if philo_wl:
            lines.append('>')
            lines.append('> **哲学**')
            for wl in sorted(philo_wl)[:4]:
                lines.append(f'> - [[{wl}]]')

        if econ_wl:
            lines.append('>')
            lines.append('> **经济学 / 文化**')
            for wl in sorted(econ_wl)[:3]:
                lines.append(f'> - [[{wl}]]')

    lines.append('')
    return '\n'.join(lines)


def gen_investment_section(overview_sections: dict[str, str]) -> str:
    """Generate 投资智慧 section."""
    lines = ['### 投资智慧', '',
             '> [!example|label:🏦 投资智慧] 50+ 年巴菲特致股东信的系统性阅读']

    quant = overview_sections.get('三、量化金融（WorldQuant）', '')
    if quant:
        wikilinks = re.findall(r'\[\[(.+?)\]\]', quant)
        seen = set()
        for wl in wikilinks:
            if wl not in seen and wl:
                seen.add(wl)
            if len(seen) >= 3:
                break
        if seen:
            lines.append('>')
            lines.append('> **量化金融**')
            for wl in sorted(seen):
                lines.append(f'> - [[{wl}]]')

    lines.append('>')
    lines.append('> **价值投资**')
    lines.append('> - [[BuffettLettersOverview]] — 1957–2024共67封年度股东信')

    lines.append('')
    return '\n'.join(lines)


def gen_reading_section(overview_sections: dict[str, str]) -> str:
    """Generate 读书笔记 section."""
    lines = ['### 读书笔记', '',
             '> [!abstract|label:📖 读书笔记] 好书值得被认真对待']

    reading = overview_sections.get('五、读书笔记：心灵与意义', '')
    if reading:
        wikilinks = re.findall(r'\[\[(.+?)\]\]', reading)
        seen = set()
        for wl in wikilinks:
            if wl not in seen and wl:
                seen.add(wl)
            if len(seen) >= 3:
                break
        for wl in sorted(seen):
            lines.append(f'> - [[{wl}]]')

    lines.append('')
    return '\n'.join(lines)


# ── manual block handling ────────────────────────────────────────────

# Default manual blocks (used on first run or when markers missing)
DEFAULT_HEADER = """---
title: JRY's digital garden
---

![[2026-04-10-hero-banner.png]]

# 欢迎来到我的数字花园

> 真正的知识不在收藏夹里，在思考的痕迹中。

你好，我是 **Zeno's Tortoise**。这不是一个博客，是我用好奇心编织的一张知识网络。

技术、哲学、投资、阅读——在这里不是孤立的分类，而是相互呼应的对话。每一篇笔记，都是我停下来认真思考的痕迹。"""

DEFAULT_QUOTES = """### 值得你停下来的一篇

> [!quote] [[忒修斯之船、阿能诃鼓、金阁寺]]
> 三千年前的印度人、十六世纪的日本人和古希腊人，在追问同一个问题：什么让一个事物保持"它自己"？

> [!quote] [[为何西方领袖常被调侃，而中国皇帝却"神圣不可侵犯"？]]
> 为什么可以调侃国王，却不能调侃教皇？答案藏在两千年的政教博弈中。

> [!quote] [[关于Transformer和MoE框架的一点思考]]
> 如果 Transformer 是一个统一的函数式，那 MoE 就是多段函数——这个类比有多准确？

> [!quote] [[读书和思考的一点思考2]]
> 二八分的不仅是时间，更是思维方式——真正的智慧发生在学科的交叉地带。"""

DEFAULT_FOOTER = """
花园的大门永远敞开。如果你被某篇笔记触动了思考，那正是这座花园存在的意义。

**Email**：jiarenyou460@gmail.com | **GitHub**：[JRY-student](https://github.com/JRY-student)"""


def read_manual_blocks() -> list[str]:
    """Read existing index.md and extract manual blocks between markers.
    Returns [header, quotes, footer]. Empty strings if not found."""
    if not INDEX_FILE.exists():
        return ["", "", ""]

    content = read_file(INDEX_FILE)
    blocks = []
    # Pattern: <!-- sync:manual --> ... <!-- sync:end -->
    for m in re.finditer(r'<!-- sync:manual -->\n(.*?)\n<!-- sync:end -->', content, re.DOTALL):
        blocks.append(m.group(1))
    return blocks if len(blocks) >= 3 else ["", "", ""]


def extract_manual_from_backup(backup_path: Path) -> list[str]:
    """Extract manual blocks from the backup index.md by finding
    the auto section boundaries."""
    content = read_file(backup_path)
    lines = content.split('\n')

    # Find boundaries
    header_end = None
    quotes_start = None
    quotes_end = None
    footer_start = None

    for i, line in enumerate(lines):
        if '都是我停下来认真思考的痕迹。' in line:
            header_end = i
        if line.strip().startswith('### 值得你停下来的一篇'):
            quotes_start = i
        if line.strip().startswith('花园的大门永远敞开'):
            footer_start = i
            quotes_end = i

    header = '\n'.join(lines[:header_end + 1]) if header_end else ""
    quotes = '\n'.join(lines[quotes_start:quotes_end]) if quotes_start and quotes_end else ""
    footer = '\n'.join(lines[footer_start:]) if footer_start else ""

    return [header, quotes, footer]


# ── main logic ───────────────────────────────────────────────────────

def regenerate_index() -> str:
    """Build the full root index.md content."""
    overview = read_file(OVERVIEW_FILE)
    overview_sections = extract_all_h2_sections(overview)

    # Try to read manual blocks from existing index.md (with markers),
    # fall back to defaults
    manual = read_manual_blocks()
    header = manual[0] if manual[0] else DEFAULT_HEADER
    quotes = manual[1] if manual[1] else DEFAULT_QUOTES
    footer = manual[2] if manual[2] else DEFAULT_FOOTER

    # Build output
    parts = []

    # Manual block 0: header
    parts.append('<!-- sync:manual -->')
    parts.append(header)
    parts.append('<!-- sync:end -->')
    parts.append('')

    # Separator
    parts.append('---')
    parts.append('')

    # Auto-generated content sections
    parts.append(gen_tech_section(overview_sections))
    parts.append(gen_philosophy_section(overview_sections))
    parts.append(gen_investment_section(overview_sections))
    parts.append(gen_reading_section(overview_sections))

    # Separator
    parts.append('---')
    parts.append('')

    # Manual block 1: quotes
    parts.append('<!-- sync:manual -->')
    parts.append(quotes)
    parts.append('<!-- sync:end -->')
    parts.append('')

    # Manual block 2: footer
    parts.append('<!-- sync:manual -->')
    parts.append(footer)
    parts.append('<!-- sync:end -->')

    return '\n'.join(parts)


def main() -> None:
    if "--init" in sys.argv:
        backup = REPO_ROOT / "index.md.bak"
        if backup.exists():
            blocks = extract_manual_from_backup(backup)
            print(f"Extracted {len([b for b in blocks if b])} manual blocks from backup")
            print(f"  Header: {len(blocks[0])} chars")
            print(f"  Quotes: {len(blocks[1])} chars")
            print(f"  Footer: {len(blocks[2])} chars")
            # Write as the initial marker-annotated index
            # We'll do this in the regenerate step
        else:
            print("No backup found at index.md.bak")
        return

    check_only = "--check" in sys.argv
    new_content = regenerate_index()

    if check_only:
        if INDEX_FILE.exists():
            old_content = read_file(INDEX_FILE)
            if old_content == new_content:
                print("index.md is in sync with overview.md ✅")
                sys.exit(0)
            else:
                print("index.md is out of sync with overview.md ❌")
                print("Run: python tools/sync-root-index.py")
                sys.exit(1)
        else:
            print("index.md does not exist. Run without --check to create it.")
            sys.exit(1)

    write_file(INDEX_FILE, new_content)
    print(f"index.md regenerated from wiki/overview.md ({date.today()})")


if __name__ == "__main__":
    main()
