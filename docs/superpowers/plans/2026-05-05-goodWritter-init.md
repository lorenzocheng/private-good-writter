# goodWritter 项目初始化实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 初始化 goodWritter 项目目录，建立完整的文档写作工作空间，包括目录结构、PDF生成管道、审阅子Agent、反馈系统和公司资料库集成。

**Architecture:** 采用简单扁平结构，使用 Python + weasyprint 实现 Markdown → HTML → PDF 转换管道，通过 Claude Code Agent 工具实现审阅子Agent，建立反馈日志系统用于持续改进。

**Tech Stack:** Python 3.10, weasyprint, markdown, Jinja2, Claude Code Agent

---

## 文件结构映射

```
goodWritter/
├── drafts/                          # 草稿目录（新建）
├── output/                          # PDF输出目录（新建）
├── docs/
│   ├── feedback/                    # 反馈日志目录（新建）
│   │   └── README.md               # 反馈系统说明
│   └── superpowers/
│       ├── specs/                   # 设计文档（已存在）
│       └── plans/                   # 实现计划（已存在）
├── scripts/                         # 工具脚本目录（新建）
│   ├── md_to_pdf.py                # Markdown转PDF脚本
│   ├── template.html               # HTML模板
│   └── style.css                   # PDF样式表
├── CLAUDE.md                       # 项目说明（需更新）
└── README.md                       # 使用指南（新建）
```

---

### Task 1: 创建目录结构

**Files:**
- Create: `drafts/` (directory)
- Create: `output/` (directory)
- Create: `docs/feedback/` (directory)
- Create: `scripts/` (directory)

- [ ] **Step 1: 创建草稿和输出目录**

```bash
cd /home/lorenzo/projects/goodWritter
mkdir -p drafts output docs/feedback scripts
```

- [ ] **Step 2: 验证目录结构**

```bash
ls -la
```

Expected: 看到 `drafts/`, `output/`, `docs/feedback/`, `scripts/` 目录

- [ ] **Step 3: 创建 .gitkeep 文件确保空目录被git跟踪**

```bash
touch drafts/.gitkeep output/.gitkeep docs/feedback/.gitkeep
```

- [ ] **Step 4: Commit**

```bash
git add drafts output docs/feedback scripts
git commit -m "feat: create directory structure for goodWritter"
```

---

### Task 2: 安装 Python 依赖

**Files:**
- Create: `requirements.txt`

- [ ] **Step 1: 创建 requirements.txt**

```txt
markdown>=3.4
weasyprint>=60.0
Jinja2>=3.1
pygments>=2.16
```

- [ ] **Step 2: 安装依赖**

```bash
cd /home/lorenzo/projects/goodWritter
pip3 install -r requirements.txt
```

- [ ] **Step 3: 验证安装**

```bash
python3 -c "import markdown; import weasyprint; import jinja2; print('All dependencies OK')"
```

Expected: 输出 "All dependencies OK"

- [ ] **Step 4: Commit**

```bash
git add requirements.txt
git commit -m "feat: add Python dependencies for PDF generation"
```

---

### Task 3: 创建 HTML 模板

**Files:**
- Create: `scripts/template.html`

- [ ] **Step 1: 创建基础 HTML 模板**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <img src="../.logo/LOGO.png" alt="毅湃科技" class="logo">
        <div class="company-name">毅湃科技（e-Pi Tech）</div>
    </header>
    
    <main>
        <h1>{{ title }}</h1>
        <div class="meta">
            <span class="date">{{ date }}</span>
            <span class="author">{{ author }}</span>
            <span class="doc-type">{{ doc_type }}</span>
        </div>
        <div class="content">
            {{ content }}
        </div>
    </main>
    
    <footer>
        <div class="page-number"></div>
        <div class="company-info">毅湃科技 | 单壁碳纳米管 | 全钒液流电池</div>
    </footer>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add scripts/template.html
git commit -m "feat: add HTML template for PDF generation"
```

---

### Task 4: 创建 CSS 样式表

**Files:**
- Create: `scripts/style.css`

- [ ] **Step 1: 创建 PDF 样式表**

```css
@page {
    size: A4;
    margin: 2.5cm;
    @top-center {
        content: "";
    }
    @bottom-center {
        content: counter(page) " / " counter(pages);
        font-size: 10pt;
        color: #666;
    }
}

body {
    font-family: "Noto Serif CJK SC", "Liberation Serif", serif;
    font-size: 12pt;
    line-height: 1.8;
    color: #333;
}

header {
    text-align: center;
    margin-bottom: 2cm;
    border-bottom: 2pt solid #0066cc;
    padding-bottom: 1cm;
}

.logo {
    width: 150px;
    height: auto;
}

.company-name {
    font-size: 14pt;
    font-weight: bold;
    color: #0066cc;
    margin-top: 0.5cm;
}

h1 {
    font-size: 24pt;
    color: #0066cc;
    text-align: center;
    margin-bottom: 1cm;
}

.meta {
    text-align: center;
    margin-bottom: 1.5cm;
    font-size: 11pt;
    color: #666;
}

.meta span {
    margin: 0 0.5cm;
}

.content {
    text-align: justify;
}

h2 {
    font-size: 16pt;
    color: #0066cc;
    border-bottom: 1pt solid #ccc;
    padding-bottom: 0.3cm;
    margin-top: 1.5cm;
}

h3 {
    font-size: 14pt;
    color: #333;
    margin-top: 1cm;
}

p {
    margin-bottom: 0.5cm;
    text-indent: 2em;
}

ul, ol {
    margin-left: 2em;
    margin-bottom: 0.5cm;
}

li {
    margin-bottom: 0.3cm;
}

footer {
    margin-top: 2cm;
    border-top: 1pt solid #ccc;
    padding-top: 0.5cm;
    font-size: 10pt;
    color: #666;
    text-align: center;
}

.company-info {
    font-style: italic;
}
```

- [ ] **Step 2: Commit**

```bash
git add scripts/style.css
git commit -m "feat: add CSS styles for PDF generation"
```

---

### Task 5: 创建 Markdown 转 PDF 脚本

**Files:**
- Create: `scripts/md_to_pdf.py`

- [ ] **Step 1: 创建转换脚本**

```python
#!/usr/bin/env python3
"""
Markdown to PDF converter for goodWritter
Usage: python3 md_to_pdf.py <input.md> [output.pdf]
"""

import sys
import os
from pathlib import Path
import markdown
from jinja2 import Template
from weasyprint import HTML

def extract_metadata(content):
    """Extract YAML frontmatter from markdown content"""
    metadata = {
        'title': '未命名文档',
        'date': '',
        'author': '毅湃科技',
        'doc_type': '文档'
    }
    
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            frontmatter = content[3:end].strip()
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    if key in metadata:
                        metadata[key] = value
            content = content[end+3:].strip()
    
    return metadata, content

def md_to_html(md_content):
    """Convert markdown to HTML"""
    extensions = [
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ]
    return markdown.markdown(md_content, extensions=extensions)

def generate_pdf(md_file, output_file=None):
    """Generate PDF from markdown file"""
    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata and content
    metadata, md_content = extract_metadata(content)
    
    # Convert markdown to HTML
    html_content = md_to_html(md_content)
    
    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir / 'template.html'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())
    
    # Render template
    full_html = template.render(
        title=metadata['title'],
        date=metadata['date'],
        author=metadata['author'],
        doc_type=metadata['doc_type'],
        content=html_content
    )
    
    # Generate PDF
    if output_file is None:
        output_file = md_file.with_suffix('.pdf')
    
    html = HTML(string=full_html, base_url=str(script_dir.parent))
    html.write_pdf(output_file)
    
    print(f"PDF generated: {output_file}")
    return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    
    if not input_file.exists():
        print(f"Error: File {input_file} not found")
        sys.exit(1)
    
    generate_pdf(input_file, output_file)
```

- [ ] **Step 2: 给脚本添加执行权限**

```bash
chmod +x scripts/md_to_pdf.py
```

- [ ] **Step 3: Commit**

```bash
git add scripts/md_to_pdf.py
git commit -m "feat: add Markdown to PDF conversion script"
```

---

### Task 6: 创建示例 Markdown 文件进行测试

**Files:**
- Create: `drafts/20260505_测试文档_示例.md`

- [ ] **Step 1: 创建测试文档**

```markdown
---
title: 毅湃科技示例文档
date: 2026-05-05
author: 程子强
doc_type: 内部文档
---

# 毅湃科技示例文档

## 一、公司简介

毅湃科技（e-Pi Tech）是一家专注于新能源材料技术的初创公司，主营业务包括单壁碳纳米管宏量制备和全钒液流电池。

## 二、核心业务

### 1. 单壁碳纳米管

- **市场定位**：高性能锂电池导电剂
- **技术优势**：国产替代，打破海外垄断
- **目标客户**：宁德时代、比亚迪等头部电池厂

### 2. 全钒液流电池

- **应用场景**：大规模储能系统
- **技术特点**：安全可靠，寿命长

## 三、团队信息

- **创始人**：程子强
- **团队规模**：3人
- **发展阶段**：Q2 2026验证窗口期

## 四、联系方式

如有任何问题，请联系创始人程子强：17302181228
```

- [ ] **Step 2: 测试 PDF 生成**

```bash
cd /home/lorenzo/projects/goodWritter
python3 scripts/md_to_pdf.py drafts/20260505_测试文档_示例.md output/20260505_测试文档_示例.pdf
```

Expected: 成功生成 PDF 文件

- [ ] **Step 3: 验证 PDF 生成**

```bash
ls -la output/
```

Expected: 看到 `20260505_测试文档_示例.pdf` 文件

- [ ] **Step 4: Commit**

```bash
git add drafts/20260505_测试文档_示例.md output/
git commit -m "feat: add sample document and test PDF generation"
```

---

### Task 7: 更新 CLAUDE.md 项目说明

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: 更新 CLAUDE.md 内容**

```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

goodWritter — 毅湃科技（e-Pi Tech）的文档写作工作空间，专注于公司对外文章的写作任务。

**公司背景**：
- 初创科技公司，主营单壁碳纳米管宏量制备和全钒液流电池
- 3人团队，目前处于Q2 2026验证窗口期
- 创始人：程子强
- 公司资料库：`~/claude-workspace/vault/`

## 文档类型

- **投资人沟通**：月度/周度简报、汇报信
- **对外合作**：技术文件、产品介绍
- **政府机构**：政策申报、人才计划材料
- **内部管理**：通知、周报、决策记录

## 工作流程

完整流程包含8个阶段：

```
用户输入提纲 → Brainstorming完善提纲 → Claude生成初稿 → 子Agent全面审阅 → 用户审核/修改 → Claude优化 → 用户确认 → 生成PDF → 记录反馈
```

### 1. 提纲阶段
用户输入初始提纲或要点，描述需要撰写的文档。

### 2. Brainstorming阶段
使用 brainstorming 技能帮助用户完善提纲：
- 确认文档目标和受众
- 补充遗漏的关键信息
- 优化结构和逻辑
- 确定最终提纲

### 3. 创作阶段
Claude 根据完善后的提纲生成完整文案，保存为 Markdown 草稿到 `drafts/` 目录。

### 4. 审阅阶段
启动子Agent进行全面审阅：
- 事实准确性（与公司信息一致性）
- 语言风格（是否符合文档类型）
- 逻辑结构
- 敏感信息检查
- 数据准确性（金额、日期、人名等）
- 生成审阅报告，标注需要修改的地方

### 5. 优化阶段
Claude 根据审阅报告自动优化内容。

### 6. 确认阶段
用户查看优化后的版本，确认或提出修改。

### 7. 输出阶段
使用 `scripts/md_to_pdf.py` 将 Markdown 转换为带公司格式的 PDF，输出到 `output/` 目录。

### 8. 反馈阶段
记录整个过程中的用户反馈到 `docs/feedback/` 目录，用于系统进化。

## 目录结构

```
goodWritter/
├── .logo/                    # 公司Logo素材
├── .template/                # PDF模板文件
├── drafts/                   # 所有草稿文件（Markdown格式）
├── output/                   # 最终PDF输出
├── scripts/                  # 工具脚本
│   ├── md_to_pdf.py         # Markdown转PDF脚本
│   ├── template.html        # HTML模板
│   └── style.css            # PDF样式表
├── docs/
│   ├── feedback/            # 反馈日志
│   └── superpowers/         # 设计文档和计划
├── CLAUDE.md                # 本文件
└── README.md                # 使用指南
```

## 文件命名规范

- **草稿**：`YYYYMMDD_文档类型_简短描述.md`
  - 示例：`20260505_投资人简报_4月月报.md`
- **输出**：`YYYYMMDD_文档类型_简短描述.pdf`
  - 示例：`20260505_投资人简报_4月月报.pdf`

## PDF生成命令

```bash
# 从Markdown生成PDF
python3 scripts/md_to_pdf.py drafts/文档名.md output/文档名.pdf

# 批量生成（示例）
for f in drafts/*.md; do
    python3 scripts/md_to_pdf.py "$f" "output/$(basename "$f" .md).pdf"
done
```

## 与公司资料库集成

**资料库位置**：`~/claude-workspace/vault/`

**关键目录**：
- `60_公司战略/` - 公司战略、决策记录、项目概览
- `70_对外宣传/` - 投资人、政府机构、合作伙伴、媒体公关
- `15_VRFB技术知识库/` - 全钒液流电池技术资料
- `30_研发项目/` - 研发项目资料

**集成方式**：
- 审阅Agent自动引用公司资料进行事实核查
- Brainstorming阶段参考公司战略和目标
- 文档内容与公司最新状态保持一致

## 反馈学习机制

反馈日志存储在 `docs/feedback/` 目录，格式：

```markdown
# 反馈日志

## YYYY-MM-DD 文档标题

### 用户反馈
- 内容方面：
- 风格方面：
- 结构方面：

### 改进措施
- 具体改进点

### 系统优化
- 对工作流程的优化建议
```

## Getting Started

1. **安装依赖**：`pip3 install -r requirements.txt`
2. **创建草稿**：在 `drafts/` 目录创建 Markdown 文件
3. **生成PDF**：运行 `python3 scripts/md_to_pdf.py drafts/文件.md output/文件.pdf`
4. **记录反馈**：在 `docs/feedback/` 目录记录使用反馈
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md with complete writing guidelines"
```

---

### Task 8: 创建反馈系统说明文档

**Files:**
- Create: `docs/feedback/README.md`

- [ ] **Step 1: 创建反馈系统说明**

```markdown
# 反馈日志系统

## 概述

本目录用于记录用户在使用 goodWritter 过程中的反馈，用于持续改进写作流程和文档质量。

## 反馈收集

### 收集时机
- 用户在确认阶段提出的修改意见
- 用户对最终PDF的评价
- 用户在使用过程中提到的任何建议

### 收集方式
- 直接记录用户反馈
- 分析用户修改的内容
- 总结用户提出的问题

## 反馈格式

每个反馈记录使用以下格式：

```markdown
# 反馈日志

## YYYY-MM-DD 文档标题

### 用户反馈
- 内容方面：
- 风格方面：
- 结构方面：

### 改进措施
- 具体改进点

### 系统优化
- 对工作流程的优化建议
```

## 反馈应用

收集的反馈将用于：
1. 更新 CLAUDE.md 中的写作规范
2. 调整审阅Agent的检查项
3. 优化 brainstorming 的引导问题
4. 改进 PDF 模板和样式
5. 积累行业特定的写作经验

## 文件命名

反馈文件使用日期命名：`YYYY-MM-DD.md`

示例：
- `2026-05-05.md`
- `2026-05-06.md`
```

- [ ] **Step 2: Commit**

```bash
git add docs/feedback/README.md
git commit -m "docs: add feedback system documentation"
```

---

### Task 9: 创建 README 使用指南

**Files:**
- Create: `README.md`

- [ ] **Step 1: 创建 README**

```markdown
# goodWritter

毅湃科技（e-Pi Tech）的文档写作工作空间，专注于公司对外文章的写作任务。

## 快速开始

### 1. 安装依赖

```bash
pip3 install -r requirements.txt
```

### 2. 创建文档

在 `drafts/` 目录创建 Markdown 文件，使用以下格式：

```markdown
---
title: 文档标题
date: 2026-05-05
author: 程子强
doc_type: 投资人简报
---

# 文档标题

正文内容...
```

### 3. 生成PDF

```bash
python3 scripts/md_to_pdf.py drafts/文档名.md output/文档名.pdf
```

## 工作流程

1. **输入提纲**：描述需要撰写的文档
2. **Brainstorming**：完善提纲，确认目标和受众
3. **生成初稿**：Claude 根据提纲生成完整文案
4. **审阅优化**：子Agent审阅，自动优化内容
5. **用户确认**：查看优化后的版本，确认或修改
6. **生成PDF**：使用模板生成带公司格式的PDF
7. **记录反馈**：记录使用反馈，用于系统进化

## 目录结构

```
goodWritter/
├── drafts/          # 草稿文件（Markdown）
├── output/          # 最终PDF输出
├── scripts/         # 工具脚本
├── docs/            # 文档目录
│   ├── feedback/    # 反馈日志
│   └── superpowers/ # 设计文档
├── .logo/           # 公司Logo
└── .template/       # PDF模板
```

## PDF格式

- **页面尺寸**：A4
- **中文字体**：Noto Serif CJK SC
- **英文字体**：Liberation Sans
- **公司Logo**：自动添加到页眉

## 与公司资料库集成

文档创作过程中会自动参考 `~/claude-workspace/vault/` 中的公司资料，确保内容准确性和一致性。

## 反馈与改进

使用过程中如有任何建议，请记录到 `docs/feedback/` 目录，帮助我们持续改进写作流程。

## 许可证

内部使用，仅限毅湃科技团队。
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add README with usage guide"
```

---

### Task 10: 最终验证

**Files:**
- None (verification only)

- [ ] **Step 1: 验证目录结构**

```bash
cd /home/lorenzo/projects/goodWritter
tree -L 2 -a
```

Expected: 看到完整的目录结构

- [ ] **Step 2: 验证 PDF 生成脚本**

```bash
python3 scripts/md_to_pdf.py --help
```

Expected: 显示使用说明

- [ ] **Step 3: 验证依赖安装**

```bash
python3 -c "import markdown; import weasyprint; import jinja2; print('All dependencies OK')"
```

Expected: 输出 "All dependencies OK"

- [ ] **Step 4: 检查 Git 状态**

```bash
git status
```

Expected: 显示所有已跟踪的文件

- [ ] **Step 5: 最终 Commit**

```bash
git add -A
git commit -m "chore: complete goodWritter project initialization"
```

---

## 执行选项

**计划已保存到 `docs/superpowers/plans/2026-05-05-goodWritter-init.md`。两种执行方式：**

**1. Subagent-Driven（推荐）** - 每个任务分配一个新鲜的子agent，任务间进行审查，快速迭代

**2. Inline Execution** - 在当前会话中执行任务，批量执行并设置检查点

**选择哪种方式？**
