# 项目类型识别模式

## 项目类型识别规则

### 前端项目 (Frontend)
**特征文件/目录:**
- `package.json` ✅ 必需
- `public/` 或 `static/` 目录
- `src/` 目录
- `index.html` 文件
- `webpack.config.js`, `vite.config.js`, `rollup.config.js`
- `tsconfig.json` (TypeScript项目)

**技术栈指标:**
- React: `react`, `react-dom`
- Vue: `vue`, `@vue/core`
- Angular: `@angular/core`
- Svelte: `svelte`
- 构建工具: `webpack`, `vite`, `parcel`, `rollup`

### 后端项目 (Backend)
**特征文件/目录:**
- `requirements.txt` (Python)
- `pom.xml` (Java Maven)
- `build.gradle` (Java Gradle)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `Gemfile` (Ruby)
- `composer.json` (PHP)

**目录结构:**
- `app/`, `src/`, `lib/` 主要代码目录
- `config/`, `conf/` 配置目录
- `migrations/` 数据库迁移 (常见于Web框架)

### 全栈项目 (Fullstack)
**特征:**
- 同时具备前端和后端特征
- `package.json` + `requirements.txt`/`pom.xml`等
- `client/`, `server/` 或 `frontend/`, `backend/` 分离的目录
- `api/` 目录
- `web/` 目录

### 移动应用项目 (Mobile)
**特征文件/目录:**
- `ios/`, `android/` (React Native, Flutter)
- `lib/` (Flutter主要代码)
- `pubspec.yaml` (Flutter)
- `android/app/build.gradle`
- `ios/Runner.xcworkspace`

### 桌面应用项目 (Desktop)
**特征文件/目录:**
- `CMakeLists.txt` (C++)
- `.pro` (Qt)
- `Form1.cs`, `MainWindow.cs` (C# WinForms)
- `MainWindow.java` (Java Swing)
- `electron` 相关配置

### 数据科学项目 (Data Science)
**特征文件/目录:**
- `requirements.txt` 包含: `pandas`, `numpy`, `scikit-learn`, `tensorflow`, `pytorch`
- `notebooks/` 目录
- `.ipynb` 文件
- `data/` 目录
- `models/` 目录

### DevOps项目
**特征文件/目录:**
- `Dockerfile`
- `docker-compose.yml`
- `kubernetes/`, `k8s/` 目录
- `.yaml`, `.yml` 文件
- `Terraform` 相关文件

## 技术栈识别模式

### JavaScript/TypeScript 生态
**包管理器:**
- `package.json` (npm/yarn)
- `yarn.lock` 或 `package-lock.json`
- `pnpm-lock.yaml`

**框架识别:**
```json
{
  "react": {
    "dependencies": ["react", "react-dom"],
    "devDependencies": ["@types/react", "webpack"]
  },
  "vue": {
    "dependencies": ["vue"],
    "devDependencies": ["@vue/cli-service", "vue-loader"]
  },
  "angular": {
    "dependencies": ["@angular/core", "@angular/common"],
    "devDependencies": ["@angular/cli"]
  }
}
```

### Python 生态
**包管理器:**
- `requirements.txt`
- `setup.py`
- `pyproject.toml`
- `Pipfile`

**框架识别:**
```
Django: django, djangorestframework
Flask: flask, flask-sqlalchemy
FastAPI: fastapi, uvicorn
```

### Java 生态
**构建工具:**
- `pom.xml` (Maven)
- `build.gradle` (Gradle)
- `build.xml` (Ant)

**框架识别:**
```xml
Spring: spring-boot-starter-*
Struts: struts-core
JSF: jsf-api
```

## Monorepo 识别
**特征:**
- `packages/` 目录
- `lerna.json` (Lerna)
- `pnpm-workspace.yaml`
- `nx.json` (Nx)
- `turbo.json` (Turborepo)

**子包结构:**
```
packages/
├── frontend/
├── backend/
├── shared/
└── docs/
```

## 配置文件识别
### 前端配置
- `tsconfig.json` - TypeScript配置
- `babel.config.js` - Babel转译配置
- `eslint.config.js` - 代码检查配置
- `prettier.config.js` - 代码格式化配置

### 后端配置
- `.env.example` - 环境变量模板
- `application.yml` - Spring Boot配置
- `settings.py` - Django配置

### 数据库配置
- `database.yml` - Rails数据库配置
- `alembic.ini` - Alembic数据库迁移配置
- `migrations/` - 数据库迁移目录

## 项目成熟度指标
### 文档完整性
- `README.md` 存在且内容丰富
- `CHANGELOG.md` 版本更新日志
- `CONTRIBUTING.md` 贡献指南
- `docs/` 目录存在且结构清晰

### 测试覆盖率
- `tests/` 或 `__tests__/` 目录
- 测试文件命名规范: `*.test.js`, `*_test.rb`, `test_*.py`
- 测试配置文件: `jest.config.js`, `pytest.ini`

### CI/CD 配置
- `.github/workflows/` (GitHub Actions)
- `.gitlab-ci.yml` (GitLab CI)
- `Jenkinsfile`
- `.travis.yml`