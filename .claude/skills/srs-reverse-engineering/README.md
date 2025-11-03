# SRS Reverse Engineering - 软件需求规格说明书反向工程生成器

## 概述

SRS Reverse Engineering 是一个专业的软件需求规格说明书反向工程技能，能够通过分析GitHub项目或本地项目代码，自动生成符合IEEE 830标准的软件需求规格说明书(SRS)。

## 核心功能

- 🔄 **项目反向工程**：自动分析项目结构、技术栈和代码实现
- 📋 **API接口提取**：智能识别REST API、GraphQL和WebSocket接口
- 🗄️ **数据库模式分析**：提取数据模型、关系和约束
- 📝 **SRS文档生成**：基于IEEE 830标准生成完整的需求规格说明书
- 🎯 **需求规格化**：将PRD转化为可作为开发合同的技术需求文档

## 使用场景

### 典型使用场景

1. **项目重构需求分析**
   ```
   "分析这个GitHub项目，生成完整的SRS文档"
   ```

2. **现有系统需求整理**
   ```
   "基于现有代码库，反向工程生成软件需求规格说明书"
   ```

3. **PRD技术化转化**
   ```
   "我有PRD文档，需要结合代码分析生成技术需求规格说明"
   ```

4. **项目文档补充**
   ```
   "帮我分析项目架构，输出标准的技术规格文档"
   ```

## 技能结构

```
srs-generator/
├── SKILL.md                    # 技能定义文件
├── scripts/                    # 分析脚本
│   ├── analyze_project_structure.py      # 项目结构分析
│   ├── extract_api_endpoints.py          # API端点提取
│   ├── analyze_database_schema.py        # 数据库模式分析
│   ├── generate_srs_sections.py          # SRS章节生成
│   └── simple_package.py                 # 技能打包脚本
├── references/                 # 参考文档
│   ├── srs-template.md                   # SRS标准模板
│   ├── functional-requirements-guide.md  # 功能需求编写指南
│   └── non-functional-requirements-checklist.md # 非功能需求清单
├── assets/                     # 模板资源
│   ├── srs-markdown-template.md           # Markdown模板
│   └── example-srs-output.md              # 示例输出文档
└── README.md                  # 使用说明
```

## 工作流程

### 第一步：项目信息收集
- 接受GitHub URL或本地项目路径
- 读取现有PRD文档（如有）
- 自动检测项目技术栈和配置

### 第二步：代码分析
1. **项目结构分析** - 使用 `analyze_project_structure.py`
2. **API端点提取** - 使用 `extract_api_endpoints.py`
3. **数据库模式分析** - 使用 `analyze_database_schema.py`

### 第三步：需求提取
- 从代码实现中提取实际功能
- 分析配置文件和环境要求
- 识别依赖关系和技术架构
- 对比PRD与实现差异

### 第四步：SRS生成
- 基于IEEE 830标准生成文档
- 包含功能性和非功能性需求
- 生成接口和数据需求
- 输出完整的Markdown格式SRS

## 使用方法

### 方式一：命令行使用

```bash
# 1. 分析项目结构
python scripts/analyze_project_structure.py /path/to/project --output project_analysis.json

# 2. 提取API端点
python scripts/extract_api_endpoints.py /path/to/project --output api_analysis.json

# 3. 分析数据库模式
python scripts/analyze_database_schema.py /path/to/project --output db_analysis.json

# 4. 生成SRS文档
python scripts/generate_srs_sections.py \
    --project project_analysis.json \
    --api api_analysis.json \
    --database db_analysis.json \
    --output srs-document.md
```

### 方式二：技能集成使用

在Claude中直接使用技能：

```
"使用srs-generator技能分析这个项目：https://github.com/user/project"
```

## SRS文档结构

生成的SRS文档包含以下标准章节：

1. **引言** - 文档目的、项目背景、术语定义
2. **总体描述** - 产品愿景、功能架构、用户特征
3. **功能性需求** - 详细的功能需求规格说明
4. **非功能性需求** - 性能、安全、可靠性需求
5. **接口需求** - 用户界面、硬件接口、软件接口
6. **数据需求** - 数据实体、关系、约束
7. **系统架构** - 技术架构、部署架构
8. **测试需求** - 测试策略、验收标准
9. **项目管理** - 开发计划、质量保证
10. **附录** - 变更历史、相关文档

## 支持的技术栈

### 前端框架
- React, Vue, Angular, Svelte
- Webpack, Vite, Babel等构建工具

### 后端框架
- Express, FastAPI, Django, Spring Boot
- Flask, NestJS等Web框架

### 数据库
- MySQL, PostgreSQL, MongoDB, SQLite
- Redis, Oracle, SQL Server

### 项目类型
- Web应用项目
- 移动应用项目
- 微服务架构
- 单体应用

## 输出示例

技能将生成标准的SRS文档，包含：

```markdown
# 项目名称 - 软件需求规格说明书

## 1. 引言
### 1.1 文档目的
### 1.2 项目背景
### 1.3 项目范围

## 3. 功能性需求
### 3.1 用户管理功能
### 3.2 数据处理功能

## 4. 非功能性需求
### 4.1 性能需求
### 4.2 安全性需求

... (更多章节)
```

## 质量保证

### 验证标准
- ✅ 符合IEEE 830标准
- ✅ 内容完整性检查
- ✅ 技术准确性验证
- ✅ 格式规范性保证

### 自动化验证
- YAML前置内容格式验证
- 文件结构完整性检查
- 内容质量评估
- 技术实现合理性验证

## 注意事项

1. **业务逻辑补充**：自动分析可能遗漏部分业务逻辑，建议结合人工审核
2. **需求验证**：建议与产品经理和开发团队共同验证生成内容
3. **文档维护**：SRS文档应随着项目进展持续更新
4. **场景适配**：非功能性需求需要根据具体业务场景定制

## 技术支持

- **技能版本**：v1.0.0
- **生成工具**：基于Python代码分析
- **文档格式**：Markdown (.md)
- **编码标准**：UTF-8

## 更新日志

### v1.0.0 (2024-01-15)
- ✅ 初始版本发布
- ✅ 支持主流技术栈分析
- ✅ 集成IEEE 830标准模板
- ✅ 完整的验证和打包流程

---

> **提示**：这个技能特别适用于项目重构、需求文档化、技术交接等场景。生成的SRS文档可以作为开发合同、测试基准和验收依据。