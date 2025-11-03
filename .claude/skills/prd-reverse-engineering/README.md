# PRD Reverse Engineering Skill

## 概述

这个技能能够从GitHub仓库或本地项目文件中反向分析出产品需求文档(PRD)。它分析代码库、文档和项目结构，生成包含项目背景、用户画像、成功指标、功能优先级和用户流程的综合性PRD。

## 主要功能

- **GitHub仓库分析**: 自动抓取和分析公开的GitHub项目
- **本地项目分析**: 扫描本地目录结构和代码文件
- **技术栈识别**: 自动识别项目使用的技术栈和框架
- **功能提取**: 从代码和文档中提取产品功能列表
- **用户画像生成**: 基于项目特点推断目标用户群体
- **PRD模板生成**: 使用标准PRD模板生成完整文档

## 使用方法

### 1. GitHub项目分析

输入GitHub仓库URL，技能会自动：
- 获取仓库基本信息（星标、Fork、描述等）
- 下载并分析README文件
- 识别编程语言和技术栈
- 分析项目结构和依赖关系
- 提取功能特性

**示例输入**:
```
请分析这个GitHub项目并生成PRD: https://github.com/microsoft/vscode
```

### 2. 本地项目分析

提供本地项目路径，技能会：
- 扫描目录结构
- 分析配置文件
- 查看代码组织方式
- 识别主要功能模块

**示例输入**:
```
请分析我的本地项目并生成PRD: /path/to/my/project
```

## 生成的PRD包含

1. **项目背景与愿景**
   - 项目概述和问题背景
   - 产品愿景和目标
   - 项目范围定义

2. **目标用户画像与场景**
   - 主要用户画像描述
   - 用户使用场景分析
   - 用户痛点和需求

3. **产品目标与成功指标**
   - 业务目标和用户目标
   - 可量化的成功指标(KPIs)
   - 技术性能指标

4. **功能列表与优先级**
   - 核心功能(P0)
   - 重要功能(P1)
   - 期望功能(P2)
   - 功能详细描述和验收标准

5. **用户流程与线框图**
   - 核心用户流程图
   - 页面布局线框图
   - 交互设计要点

## 技能文件结构

```
prd-reverse-engineering/
├── SKILL.md                    # 技能主文件
├── scripts/
│   └── analyze_github_repo.py   # GitHub仓库分析脚本
├── references/
│   ├── prd_structure_guide.md   # PRD结构详细指南
│   ├── feature_extraction_methods.md  # 功能提取方法
│   └── user_persona_templates.md       # 用户画像模板
├── assets/
│   └── prd_template.md          # PRD模板
└── README.md                   # 本文档
```

## 工具和脚本

### GitHub分析脚本

**位置**: `scripts/analyze_github_repo.py`

**功能**:
- 获取GitHub仓库基本信息
- 分析README内容
- 识别技术栈和依赖
- 提取功能特性
- 评估项目复杂度和成熟度

**使用方法**:
```bash
python scripts/analyze_github_repo.py <github_url>
```

**输出示例**:
```json
{
  "repository": {
    "name": "vscode",
    "description": "Visual Studio Code",
    "stars": 178150,
    "language": "TypeScript"
  },
  "technology": {
    "tech_stack": {
      "frontend": ["typescript", "javascript"],
      "backend": [],
      "frameworks": ["Electron"]
    }
  },
  "analysis": {
    "project_type": "Desktop Application",
    "complexity": "High",
    "maturity": "Mature"
  }
}
```

## 参考文档

### PRD结构指南
详细的PRD各章节写作指南，包括：
- 内容要求和写作要点
- 质量检查清单
- 最佳实践建议

### 功能提取方法
系统性的功能识别和分析方法：
- 代码结构分析策略
- 用户界面功能识别
- 功能分类和优先级评估
- 质量保证检查清单

### 用户画像模板
完整的用户画像创建模板：
- 基础信息模板
- 产品相关模板
- 行为模式分析
- 专项用户画像(B2C/B2B)

## 依赖要求

- Python 3.13+
- requests >= 2.31.0

## 权限要求

技能需要以下权限：
- `WebFetch`: 获取GitHub仓库信息
- `Glob`: 搜索文件模式
- `Grep`: 搜索文件内容
- `Read`: 读取文件内容
- `Write`: 生成PRD文档
- `Task`: 启动专门的代理进行复杂分析

## 使用示例

### 示例1: 分析开源项目

**用户输入**:
```
请帮我分析这个GitHub项目并生成PRD: https://github.com/facebook/react
```

**技能输出**:
- 完整的PRD文档
- React项目的技术分析
- 目标用户群体识别
- 功能模块梳理

### 示例2: 分析本地项目

**用户输入**:
```
我有一个电商项目，请帮我生成PRD，项目在: ./my-ecommerce-app
```

**技能输出**:
- 基于本地代码的PRD
- 用户画像和场景分析
- 功能优先级建议
- 用户流程设计

## 最佳实践

1. **提供完整信息**: 尽量提供完整的项目URL或路径
2. **明确分析重点**: 可以指定需要重点分析的功能模块
3. **迭代完善**: 可以基于生成的PRD进行进一步的细化和调整
4. **结合业务知识**: 将自动分析结果与实际业务需求结合

## 局限性

- 只能分析公开的GitHub仓库
- 对于缺少文档的项目，分析准确性可能降低
- 复杂的业务逻辑需要人工验证
- 生成的用户画像可能需要根据实际用户数据调整

## 更新日志

### v1.0.0 (2025-11-03)
- 初始版本发布
- 支持GitHub仓库分析
- 提供完整的PRD模板
- 包含用户画像和功能提取方法

---

*这个技能由Claude Skills Demo项目维护，用于演示Claude技能开发能力。*