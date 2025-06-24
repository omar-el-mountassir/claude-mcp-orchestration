# Complete Project Setup

Set up a new project with best practices: $ARGUMENTS

## Project Initialization:

### 1. Project Structure
```
$ARGUMENTS/
├── src/
│   ├── components/
│   ├── services/
│   ├── utils/
│   └── index.ts
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   └── CONTRIBUTING.md
├── scripts/
├── .github/
│   └── workflows/
├── .env.example
├── .gitignore
├── README.md
├── package.json
└── tsconfig.json
```

### 2. Version Control
- Initialize git repository
- Create .gitignore with appropriate patterns
- Set up branch protection rules
- Create initial commit

### 3. Dependencies
- Initialize package manager (npm/yarn/pnpm)
- Add essential dependencies
- Set up TypeScript (if applicable)
- Configure build tools

### 4. Development Environment
- Set up ESLint with team rules
- Configure Prettier
- Add husky for git hooks
- Set up lint-staged

### 5. Testing Framework
- Install Jest/Vitest or preferred framework
- Configure test runners
- Add coverage requirements
- Create example tests

### 6. CI/CD Pipeline
- Create GitHub Actions workflow
- Add test automation
- Configure deployment stages
- Set up environment secrets

### 7. Documentation
- Create comprehensive README
- Add API documentation template
- Include contribution guidelines
- Set up changelog

### 8. Development Scripts
```json
{
  "scripts": {
    "dev": "development server",
    "build": "production build",
    "test": "run tests",
    "lint": "lint code",
    "format": "format code"
  }
}
```

### 9. Claude Integration
- Create .claude/commands/ directory
- Add project-specific workflows
- Configure MCP if needed
- Document AI workflows

Use think hard for architectural decisions.