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
使用 `node scripts/gen_docx.js` 将 Markdown 转换为带公司格式的 Word 文档，输出到 `output/` 目录。

### 8. 反馈阶段
记录整个过程中的用户反馈到 `docs/feedback/` 目录，用于系统进化。

## 目录结构

```
goodWritter/
├── .logo/                    # 公司Logo素材
├── drafts/                   # 所有草稿文件（Markdown格式）
├── output/                   # 最终Word文档输出
├── scripts/                  # 工具脚本
│   ├── gen_docx.js          # Markdown转Word脚本
│   └── template.typ         # Typst排版模板（备用）
├── docs/
│   ├── feedback/            # 反馈日志
│   └── superpowers/         # 设计文档和计划
├── CLAUDE.md                # 本文件
└── README.md                # 使用指南
```

## 文件命名规范

- **草稿**：`YYYYMMDD_文档类型_简短描述.md`
  - 示例：`20260505_投资人简报_4月月报.md`
- **输出**：`YYYYMMDD_文档类型_简短描述.docx`
  - 示例：`20260505_投资人简报_4月月报.docx`

## Word文档生成命令

```bash
# 从Markdown生成Word文档
node scripts/gen_docx.js

# 如需修改输入文件，编辑 scripts/gen_docx.js 中的路径
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

1. **安装依赖**：`pip3 install -r requirements.txt` && `npm install`
2. **创建草稿**：在 `drafts/` 目录创建 Markdown 文件
3. **生成Word文档**：运行 `node scripts/gen_docx.js`
4. **记录反馈**：在 `docs/feedback/` 目录记录使用反馈
