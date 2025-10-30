# Project Analyzer Skill

一个用于软件项目解构与需求分析的Claude Skill，扮演产品经理角色来分析项目结构、功能特性和商业可行性。

## 功能特性

### P0 核心功能 (MVP)
- **许可证合规性分析** - 识别项目许可证类型，评估商用风险
- **项目活跃度分析** - 分析提交历史、Issue状态，判断维护状态
- **安装与启动总结** - 提取关键安装步骤和启动命令

### P1 重要功能
- **贡献者分析** - 识别主要贡献者和社区参与度
- **模块依赖分析** - 分析外部依赖和内部模块关系

### 报告类型
- **完整分析报告** - 综合项目评估
- **商业评估报告** - 专注商业可行性
- **快速摘要** - 核心信息概览
- **开发者上手指南** - 架构和启动重点

## 使用方法

### 综合项目分析
```
你帮我分析一下这个项目：[项目路径]。它主要做什么的？用什么技术？是否还在积极维护？
```

### 商业可行性评估
```
我正在评估是否在我的公司里使用这个开源库：[项目路径]。帮我重点分析一下它的许可证是否允许商用，以及这个社区是否活跃。
```

### 开发者快速上手
```
我需要快速上手 [项目路径] 这个项目。帮我总结一下它的核心架构和本地启动的步骤。
```

## 技术架构

### Scripts (可执行脚本)
- `analyze_project.py` - 主分析脚本，检测项目类型和Git活动
- `dependency_parser.py` - 依赖解析器，支持多种包管理器
- `license_analyzer.py` - 许可证分析器，识别常见开源许可证

### References (参考资料)
- `license_templates.md` - 常见许可证参考和商用风险评估
- `project_type_patterns.md` - 项目类型识别模式和技术栈特征

### Assets (报告模板)
- `full_analysis.md` - 完整分析报告模板
- `commercial_evaluation.md` - 商业评估专用模板
- `quick_summary.md` - 快速摘要模板

## 支持的项目类型

- **前端项目** - React, Vue, Angular, Svelte等
- **后端项目** - Node.js, Python, Java, Go等
- **全栈项目** - 前后端分离架构
- **移动应用** - React Native, Flutter等
- **数据科学项目** - Jupyter notebooks, ML项目等

## 许可证识别支持

- MIT License
- Apache 2.0
- GPL-3.0 / GPL-2.0
- BSD-3-Clause
- ISC License
- 专有许可证识别

## 输出格式

所有报告均采用Markdown格式，便于：
- 复制到文档工具 (Notion, Typora)
- 版本控制管理
- 团队协作分享

## 注意事项

- 对于私有项目，可能需要手动提供关键文件内容
- Git历史分析需要项目包含`.git`目录
- 许可证分析基于文本模式匹配，建议人工验证重要项目

## 技术要求

- Python 3.6+
- Git (用于历史分析)
- 支持Windows、macOS、Linux

---

*Created with Claude Code Skill Creator*