# Scaffold Frontend Project

## Purpose
Generate complete frontend project structure with Clean Architecture + DDD principles.

**CRITICAL**: Always use Next.js 16+ with App Router as the default framework. Only use pure React + Vite when user explicitly mentions offline-first functionality or specifically requests non-Next.js setup.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - project_name
  - features
optional_params:
  - pwa_enabled
  - theme_config
```

## Task Execution

### Step 1: Elicit Project Requirements
Ask user for the following information:

**Project Name**: What would you like to name your frontend project?
**Initial Features**: List the main features/modules you want to start with (e.g., auth, dashboard, profile)
**PWA Enabled**: Do you want Progressive Web App capabilities? (default: yes)
**Theme Configuration**: Do you have specific theme/brand requirements?

### Step 2: Generate Project Structure
Create the following folder structure:

```
src/
├── features/
│   └── shared/
│       ├── components/
│       ├── hooks/
│       ├── utils/
│       └── types/
├── app/
│   ├── providers/
│   ├── router/
│   └── store/
└── infrastructure/
    ├── api/
    ├── storage/
    └── pwa/
```

### Step 3: Setup Configuration Files
- Initialize Next.js 16+ project with TypeScript
- Configure Next.js config for App Router
- Setup TailwindCSS + Shadcn/ui integration
- Configure Vitest for testing (with Next.js)
- Setup ESLint + Prettier (Next.js config)
- Configure PWA with Next.js PWA plugin if requested
- Setup environment configuration

### Step 4: Generate Initial Features
For each feature requested:
- Create feature folder with DDD structure
- Generate basic domain entities
- Create application layer with hooks and stores
- Setup infrastructure layer with API clients
- Create presentation layer with basic components

### Step 5: Validation
- Verify all files compile without errors
- Run initial tests
- Check TypeScript strict mode compliance
- Validate folder structure follows Clean Architecture

## Completion Criteria
- Project structure matches Clean Architecture patterns
- All dependencies are properly installed
- Initial features are scaffolded with all layers
- TypeScript compiles without errors
- Basic tests pass