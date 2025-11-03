---
name: prd-reverse-engineering
description: This skill should be used when users need to reverse-engineer a Product Requirements Document (PRD) from an existing GitHub repository or local project files. The skill analyzes codebases, documentation, and project structure to generate comprehensive PRDs including project background, user personas, success metrics, feature prioritization, and user workflows with wireframes. Use this skill when users provide GitHub URLs or project directories and request product analysis or PRD generation.
license: MIT
allowed-tools:
  - WebFetch
  - Glob
  - Grep
  - Read
  - Write
  - Task
metadata:
  version: "1.0.0"
  author: "Claude Skills Demo"
  tags: ["product-management", "reverse-engineering", "documentation", "analysis"]
  category: "product-development"
---

# PRD Reverse Engineering Skill

## Overview

This skill transforms existing codebases and project artifacts into comprehensive Product Requirements Documents (PRDs). It analyzes GitHub repositories or local project files to extract product insights, user needs, and business objectives, then structures them into a professional PRD format.

## When to Use This Skill

Use this skill when users:
- Provide a GitHub URL and ask for product analysis or PRD generation
- Share a local project directory and request reverse-engineering of requirements
- Want to understand the product vision behind an existing codebase
- Need to create product documentation from legacy projects
- Are conducting product audits or competitive analysis

## Core Workflow

### Phase 1: Project Discovery and Analysis

1. **Accept Input**: Receive GitHub URL or local project path from user
2. **Initial Discovery**:
   - For GitHub: Fetch repository metadata, README, and main documentation
   - For Local: Scan directory structure, key files, and documentation
3. **Technology Stack Analysis**: Identify technologies, frameworks, and architectural patterns
4. **Scope Assessment**: Determine project size, complexity, and analysis depth required

### Phase 2: Deep Codebase Analysis

1. **Code Structure Analysis**:
   - Examine file organization and module structure
   - Identify main features and functionality
   - Analyze data models and business logic
   - Review API endpoints and interfaces

2. **Documentation Mining**:
   - Extract information from README files
   - Analyze inline documentation and comments
   - Review configuration files and package metadata
   - Study existing user guides or API docs

3. **User Interface Analysis**:
   - Identify UI components and user flows
   - Analyze screen layouts and interaction patterns
   - Document responsive design considerations

### Phase 3: Product Intelligence Synthesis

1. **Target User Identification**:
   - Analyze user roles and permissions
   - Identify user pain points addressed
   - Document user scenarios and use cases

2. **Business Objectives Extraction**:
   - Identify core problems being solved
   - Extract success metrics and KPIs
   - Document competitive differentiators

3. **Feature Prioritization**:
   - Map features to user needs
   - Identify core vs. advanced functionality
   - Assess implementation complexity

### Phase 4: PRD Generation

1. **Structure Creation**: Use PRD template from `assets/prd_template.md`
2. **Content Population**: Fill each section with synthesized insights
3. **Validation**: Ensure completeness and coherence
4. **Output Generation**: Create final PRD document

## Working with Bundled Resources

### Scripts (`scripts/`)

- **analyze_github_repo.py**: Automated GitHub repository analysis script
- **extract_features.py**: Feature extraction from codebase analysis
- **generate_user_flows.py**: User flow diagram generation helper

### References (`references/`)

- **prd_structure_guide.md**: Detailed PRD section explanations and best practices
- **feature_extraction_methods.md**: Systematic approaches to identifying features
- **user_persona_templates.md**: Templates for creating detailed user personas
- **metrics_framework.md**: Framework for defining product success metrics

### Assets (`assets/`)

- **prd_template.md**: Comprehensive PRD template with placeholders
- **wireframe_templates/**: Basic wireframe templates for common UI patterns
- **persona_cards.md**: User persona template cards

## Output Format

Generate a comprehensive PRD document with the following sections:

1. **项目背景与愿景** (Project Background & Vision)
2. **目标用户画像与场景** (Target User Personas & Scenarios)
3. **产品目标与成功指标** (Product Goals & Success Metrics)
4. **功能列表与优先级** (Feature List & Priorities)
5. **用户流程与线框图** (User Flows & Wireframes)

## Usage Guidelines

1. **Always start** by understanding the user's specific context and needs
2. **Use progressive disclosure** - start with high-level analysis, then drill down
3. **Leverage bundled resources** to ensure consistency and completeness
4. **Validate assumptions** with the user when critical information is missing
5. **Iterate and refine** based on user feedback

## Quality Assurance

- Ensure all PRD sections are completed with meaningful content
- Validate that features identified match the actual codebase functionality
- Confirm user personas are consistent with the product's actual user base
- Verify that success metrics are measurable and aligned with business objectives
- Check that user flows reflect actual implementation capabilities