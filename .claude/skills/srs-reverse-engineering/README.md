# SRS逆向工程自动化技能

## 概述

这是一个通过逆向工程自动分析现有代码库，生成标准化软件需求规格说明书（SRS）的技能包。当项目缺乏技术文档、需要为遗留系统补全需求分析，或为重构升级准备需求文档时，本技能可以显著提高工作效率。

## 功能特性

### 🔍 **多维度代码分析**
- **数据库逆向工程**: 自动识别数据表、字段关系和业务约束
- **API接口发现**: 智能识别REST API端点和外部服务依赖
- **代码结构分析**: 分析系统架构模式和核心业务逻辑
- **业务规则提取**: 自动提取验证、计算、授权等业务规则

### 📊 **标准化文档生成**
- 基于IEEE 830标准的SRS模板
- 功能需求自动推导和文档化
- 非功能需求基于代码证据推断
- 数据字典和实体关系图自动生成

### 🛠 **多技术栈支持**
- **后端框架**: Express.js, FastAPI, Django, Spring Boot, Gin等
- **数据库**: MySQL, PostgreSQL, MongoDB, Prisma ORM等
- **编程语言**: Python, JavaScript/TypeScript, Java, Go等

## 安装和使用

### 环境要求
- Python 3.7+
- 标准库: `json`, `re`, `os`, `pathlib`, `datetime`
- 可选依赖: `pyyaml` (用于OpenAPI文件解析)

### 基本使用流程

1. **准备项目环境**
   ```bash
   # 确保Python环境
   python --version
   ```

2. **执行完整分析**
   ```bash
   # 步骤1: 数据库分析
   python scripts/analyze_database.py /path/to/your/project --output ./analysis/database

   # 步骤2: API发现
   python scripts/discover_apis.py /path/to/your/project --output ./analysis/api

   # 步骤3: 代码结构分析
   python scripts/analyze_code_structure.py /path/to/your/project --output ./analysis/code

   # 步骤4: 生成SRS文档
   python scripts/generate_srs_template.py --analysis ./analysis --output ./SRS_DOCUMENT.md
   ```

3. **质量检查**
   - 使用 `assets/srs_checklist.md` 进行文档质量检查
   - 参考 `references/` 目录下的分析指南

## 技能结构

```
srs-reverse-engineering/
├── SKILL.md                    # 主技能文件，包含完整工作流程
├── README.md                   # 技能说明文档
├── scripts/                    # 自动化分析脚本
│   ├── analyze_database.py     # 数据库逆向工程分析
│   ├── discover_apis.py        # API接口自动发现
│   ├── analyze_code_structure.py # 代码结构和业务逻辑分析
│   └── generate_srs_template.py # SRS文档自动生成
├── references/                 # 分析参考资料和指南
│   ├── srs_template.md         # 标准SRS文档模板
│   ├── analysis_guidelines.md  # 详细分析方法论
│   ├── business_rules_extraction.md # 业务规则提取指南
│   └── nfr_identification.md   # 非功能需求识别指南
└── assets/                     # 质量控制和资源文件
    └── srs_checklist.md        # SRS质量检查清单
```

## 分析脚本详解

### 1. 数据库分析脚本 (`analyze_database.py`)
**功能**: 自动分析数据库结构，生成ERD和数据字典

**支持格式**:
- SQL创建脚本 (*.sql)
- Prisma Schema文件
- 数据库迁移文件

**输出**:
- `erd.md`: Mermaid格式的实体关系图
- `data_dictionary.md`: 详细的数据字典
- `database_analysis.json`: 结构化分析数据

### 2. API发现脚本 (`discover_apis.py`)
**功能**: 自动发现和文档化API端点

**支持框架**:
- Node.js: Express.js, Fastify, Koa
- Python: Flask, FastAPI, Django
- Java: Spring Boot, JAX-RS
- Go: Gin, Echo, Fiber

**输出**:
- `api_documentation.md`: 完整的API文档
- `api_analysis.json`: 结构化API数据

### 3. 代码结构分析脚本 (`analyze_code_structure.py`)
**功能**: 分析项目架构和提取业务规则

**分析内容**:
- 项目架构模式识别
- 类和函数结构分析
- 业务规则自动提取
- 依赖关系分析

**输出**:
- `code_structure_analysis.md`: 架构分析报告
- `code_analysis.json`: 详细代码分析数据

### 4. SRS生成脚本 (`generate_srs_template.py`)
**功能**: 基于分析结果生成标准化SRS文档

**整合内容**:
- 项目概述和技术栈信息
- 功能需求（基于API和业务规则）
- 非功能需求（基于代码模式推断）
- 数据需求（基于数据库分析）

## 使用示例

### 示例1: 分析Web应用项目
```bash
# 假设有一个Express.js项目在 /home/user/my-webapp
python scripts/analyze_database.py /home/user/my-webapp --output ./analysis
python scripts/discover_apis.py /home/user/my-webapp --output ./analysis
python scripts/analyze_code_structure.py /home/user/my-webapp --output ./analysis
python scripts/generate_srs_template.py --analysis ./analysis --output ./SRS.md
```

### 示例2: 分析Java Spring Boot项目
```bash
# 对于Maven项目
python scripts/discover_apis.py /home/user/my-spring-app --output ./analysis
python scripts/analyze_code_structure.py /home/user/my-spring-app --output ./analysis
```

## 输出文档说明

生成的SRS文档包含以下主要章节：

1. **引言**: 项目背景、目的和范围
2. **总体描述**: 产品功能、用户特征、运行环境
3. **功能需求**: 基于API和业务规则的具体需求
4. **外部接口需求**: API接口和外部依赖
5. **非功能需求**: 性能、安全、可靠性等要求
6. **数据需求**: 数据字典和实体关系

## 质量保证

### 质量检查清单
使用 `assets/srs_checklist.md` 进行全面的质量检查，包括：
- 文档完整性检查
- 功能需求准确性验证
- 非功能需求合理性评估
- 格式和表达规范检查

### 局限性说明
- 基于静态代码分析，可能遗漏动态行为
- 部分需求需要人工确认和补充
- 推断的非功能需求需要实际测试验证

## 最佳实践

### 分析前准备
1. 确保项目代码完整可访问
2. 了解项目的基本技术栈
3. 准备充足的分析时间和存储空间

### 分析过程
1. 按顺序执行各个分析脚本
2. 检查每个脚本的输出结果
3. 遇到错误时查看日志并调整参数

### 结果验证
1. 与项目相关人员确认关键需求
2. 通过实际运行验证分析结果
3. 根据反馈调整和补充文档

## 故障排除

### 常见问题

**Q: 脚本执行提示权限错误**
A: 确保对项目目录有读取权限，对输出目录有写入权限

**Q: 分析结果为空**
A: 检查项目路径是否正确，确认代码文件存在且可访问

**Q: 生成的SRS文档内容不完整**
A: 检查各个分析脚本是否都成功执行，查看分析输出的JSON文件

**Q: 支持哪些技术栈**
A: 目前支持主流的Web开发框架，具体清单请参考各脚本的文档

## 贡献指南

### 技能扩展
要扩展技能以支持新的技术栈或分析维度：

1. 在 `scripts/` 目录下添加新的分析脚本
2. 更新 `references/` 目录下的相关指南
3. 修改 `SKILL.md` 中的工作流程
4. 更新 `README.md` 文档

### 脚本开发规范
- 使用Python 3.7+语法
- 提供详细的命令行参数说明
- 包含错误处理和日志输出
- 生成标准化的JSON输出格式

## 版本历史

### v1.0.0 (当前版本)
- 基础的数据库、API、代码结构分析功能
- 标准SRS文档自动生成
- 支持主流Web开发框架

## 许可证

本技能包遵循MIT许可证。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 创建GitHub Issue
- 发送邮件至技能维护者

---

**注意**: 本技能生成的SRS文档基于代码逆向工程分析，反映的是系统的当前实现状态。建议在使用前与项目相关人员进行确认，以确保文档的准确性和完整性。