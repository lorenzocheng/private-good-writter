# goodWritter

毅湃科技（e-Pi Tech）的文档写作工作空间，专注于公司对外文章的写作任务。

## 快速开始

### 1. 安装依赖

```bash
pip3 install -r requirements.txt
npm install  # 安装Node.js依赖
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

正文内容...
```

### 3. 生成Word文档

```bash
node scripts/gen_docx.js
```

## 工作流程

1. **输入提纲**：描述需要撰写的文档
2. **Brainstorming**：完善提纲，确认目标和受众
3. **生成初稿**：Claude 根据提纲生成完整文案
4. **审阅优化**：子Agent审阅，自动优化内容
5. **用户确认**：查看优化后的版本，确认或修改
6. **生成Word文档**：使用模板生成带公司格式的Word文档
7. **记录反馈**：记录使用反馈，用于系统进化

## 目录结构

```
goodWritter/
├── drafts/          # 草稿文件（Markdown）
├── output/          # 最终Word文档输出
├── scripts/         # 工具脚本
├── docs/            # 文档目录
│   ├── feedback/    # 反馈日志
│   └── superpowers/ # 设计文档
├── .logo/           # 公司Logo
├── CLAUDE.md        # 项目说明
└── README.md        # 使用指南
```

## Word文档格式

- **页面尺寸**：A4
- **中文字体**：宋体
- **英文字体**：Arial
- **公司Logo**：自动添加到页眉
- **所有文字**：黑色

## 与公司资料库集成

文档创作过程中会自动参考 `~/claude-workspace/vault/` 中的公司资料，确保内容准确性和一致性。

## 反馈与改进

使用过程中如有任何建议，请记录到 `docs/feedback/` 目录，帮助我们持续改进写作流程。

## 许可证

内部使用，仅限毅湃科技团队。
