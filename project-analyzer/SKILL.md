---
name: project-analyzer
description: This skill specializes in project deconstruction and requirements analysis. It analyzes software projects from a product manager perspective, focusing on understanding user needs, business problems, functional design, and how requirements are translated into technical implementations. The skill helps users learn how to analyze project requirements and apply these insights to their own product development.
---

# 项目解构与需求分析器

这个技能专注于从产品经理的角度解构项目，深入分析用户需求、业务问题、功能设计，以及需求如何转化为技术实现。帮助用户学习需求分析方法论，为自己的项目开发提供参考。

**重要提醒：此技能的所有输出必须使用简体中文，不能使用英文或emoji符号。**

## 使用场景

在以下情况下使用此技能：

### GitHub项目分析
- 分析开源GitHub项目的需求设计和用户需求
- 学习成功项目的功能设计和商业模式
- 理解开源项目的用户群体和价值主张
- 分析竞品GitHub项目的产品策略

### 本地项目分析
- 分析本地项目目录的需求设计
- 解构自己或团队项目的功能架构
- 学习项目需求分析的方法论
- 为项目重构和功能扩展提供参考

### 学习和参考
- 学习如何将用户需求转化为产品功能
- 理解项目的商业价值主张和用户场景
- 分析产品功能背后的业务逻辑
- 为自己的项目做需求分析和功能规划
- 学习产品经理的思维方式和工作方法

## 核心分析内容

### 1. 用户需求分析
- 识别目标用户群体和用户画像
- 分析用户的核心痛点和需求
- 理解用户使用场景和用户旅程
- 分析用户价值主张

### 2. 业务问题解构
- 识别项目要解决的核心业务问题
- 分析问题的严重性和紧迫性
- 理解业务模式和盈利逻辑
- 分析市场规模和商业机会

### 3. 功能设计分析
- 解构核心功能模块
- 分析功能优先级和依赖关系
- 理解功能如何满足用户需求
- 分析功能设计的合理性

### 4. 用户体验分析
- 分析用户界面和交互设计
- 理解用户体验流程
- 识别用户痛点和优化点
- 分析易用性和可访问性

### 5. 需求到技术映射
- 分析业务需求如何转化为技术功能
- 理解技术选型如何支撑业务需求
- 分析系统架构对需求的支撑能力
- 识别技术实现中的需求权衡

## 报告类型

### 需求分析报告 (`requirements`) - 完整的需求分析
- 用户需求深度分析
- 业务问题解构
- 功能设计分析
- 产品定位和价值主张

### 竞品分析报告 (`competitor`) - 竞争对手分析
- 竞品功能对比
- 差异化优势分析
- 市场定位分析
- 学习借鉴要点

### 用户场景分析 (`scenario`) - 用户场景深度分析
- 典型用户画像
- 核心使用场景
- 用户旅程分析
- 场景背后的需求

## 报告生成要求

**所有报告必须保存为Markdown文件到项目根目录的 `reports/` 文件夹中，使用简体中文，专注需求分析。**

### 文件命名规范
- `{项目名称}_requirements_analysis_{时间戳}.md` - 需求分析报告
- `{项目名称}_competitor_analysis_{时间戳}.md` - 竞品分析报告
- `{项目名称}_scenario_analysis_{时间戳}.md` - 用户场景分析

### 报告输出路径
- **默认位置**: 项目根目录下的 `reports/` 文件夹
- **完整路径示例**: `/项目根目录/reports/项目名称_requirements_analysis_20240128_143000.md`
- **自动创建**: 如果 `reports/` 目录不存在，会自动创建

## 分析方法

### 1. 用户需求分析方法
- 用户画像构建
- 用户旅程映射
- 痛点分析
- 需求优先级排序

### 2. 功能解构方法
- 功能模块划分
- 核心功能识别
- 功能依赖分析
- 用户价值评估

### 3. 业务分析方法
- 商业模式画布
- 价值主张分析
- 收入模式分析
- 成本结构分析

## 支持的分析目标

### 1. GitHub项目分析
支持各种GitHub URL格式：
- `https://github.com/facebook/react`
- `facebook/react`
- `https://github.com/vuejs/vue/core`

### 2. 本地项目目录分析
支持本地项目目录路径：
- `/path/to/myproject`
- `./myproject`
- `C:\Projects\myapp`

## 实用工作流程

### GitHub项目分析示例
```
用户: 我想分析这个GitHub项目的需求设计：https://github.com/facebook/react

Claude执行流程：
1. **GitHub项目信息获取** - 获取仓库基本信息、星标数、语言等
2. **项目文件下载** - 克隆或下载README、配置文件等
3. **项目定位分析** - 理解项目的市场定位和目标用户
4. **用户需求识别** - 分析用户的核心需求和痛点
5. **功能解构** - 分析功能如何满足用户需求
6. **商业价值分析** - 理解项目的商业逻辑和价值主张
7. **需求分析报告** - 生成需求分析文档
8. **保存到reports目录** - 确保文件正确保存
9. **提供文件路径** - 告知用户分析报告的位置
```

### 本地项目分析示例
```
用户: 分析我这个项目的需求设计：/path/to/myproject

Claude执行流程：
1. **本地项目扫描** - 扫描项目目录结构和文件
2. **项目类型识别** - 识别项目类型和技术栈
3. **项目定位分析** - 理解项目的市场定位和目标用户
4. **用户需求识别** - 分析用户的核心需求和痛点
5. **功能解构** - 分析功能如何满足用户需求
6. **商业价值分析** - 理解项目的商业逻辑和价值主张
7. **需求分析报告** - 生成需求分析文档
8. **保存到reports目录** - 确保文件正确保存
9. **提供文件路径** - 告知用户分析报告的位置
```

## 核心脚本使用

### 分析脚本
- `analyze_project.py` - 本地项目结构和功能分析
- `github_analyzer.py` - GitHub项目分析（支持克隆和文件下载）
- `dependency_parser.py` - 技术栈和依赖分析
- `license_analyzer.py` - 许可证分析
- `simple_report_generator.py` - 需求分析报告生成器

### GitHub项目分析示例
```python
from scripts.github_analyzer import GitHubAnalyzer
from scripts.simple_report_generator import SimpleReportGenerator

# 分析GitHub项目
github_analyzer = GitHubAnalyzer()
github_url = "https://github.com/facebook/react"

# 获取项目分析数据
analysis_result = github_analyzer.analyze_github_project(github_url)

# 整理需求数据
requirements_data = {
    "PROJECT_NAME": analysis_result["github_info"]["name"],
    "PROJECT_POSITIONING": analysis_result["github_info"]["description"],
    "TARGET_USERS": "从README和项目结构分析得出",
    "USER_NEEDS": "从项目功能分析得出",
    # ... 其他需求分析数据
}

# 生成需求分析报告
generator = SimpleReportGenerator(".")
report_path = generator.create_report_from_template(
    analysis_result["github_info"]["name"],
    "requirements",
    requirements_data
)
```

### 本地项目分析示例
```python
from scripts.analyze_project import ProjectAnalyzer
from scripts.simple_report_generator import SimpleReportGenerator

# 分析本地项目
project_path = "/path/to/local/project"
analyzer = ProjectAnalyzer(project_path)
analysis_result = analyzer.generate_full_analysis()

# 整理需求数据并生成报告
generator = SimpleReportGenerator(".")
report_path = generator.create_report_from_template("项目名称", "requirements", requirements_data)
```

## 输出要求

- **需求导向**: 专注于用户需求和业务问题
- **产品思维**: 从产品经理角度进行分析
- **功能解构**: 深入分析功能设计背后的需求逻辑
- **用户中心**: 始终围绕用户价值和用户体验
- **实用洞察**: 提供可用于自己项目需求分析的洞察

**绝对禁止在对话中直接输出完整的分析报告！所有需求分析报告必须保存到项目根目录的 `reports/` 文件夹中。**