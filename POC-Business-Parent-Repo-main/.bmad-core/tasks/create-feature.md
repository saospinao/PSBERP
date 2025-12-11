# Create Frontend Feature

## Purpose
Create a complete feature following Clean Architecture + DDD principles with all necessary layers.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - feature_name
  - entities
  - use_cases
optional_params:
  - api_endpoints
  - ui_components
```

## Task Execution

### Step 1: Elicit Feature Requirements
Ask user for:

**Feature Name**: What is the name of the feature? (use kebab-case)
**Domain Entities**: What are the main business entities for this feature?
**Use Cases**: What are the main use cases/operations users can perform?
**API Endpoints**: What backend endpoints will this feature consume? (optional)
**UI Components**: Any specific components you know you'll need? (optional)

### Step 2: Create Feature Structure
Generate the following structure:

```
src/features/{feature_name}/
├── domain/
│   ├── entities/
│   ├── repositories/
│   ├── services/
│   └── types/
├── application/
│   ├── use-cases/
│   ├── hooks/
│   └── store/
├── infrastructure/
│   ├── repositories/
│   ├── api/
│   └── adapters/
└── presentation/
    ├── components/
    ├── pages/
    └── styles/
```

### Step 3: Generate Domain Layer
For each entity:
- Create TypeScript interfaces/types
- Define value objects if needed
- Create repository interfaces
- Define domain services if complex business rules exist

### Step 4: Generate Application Layer
For each use case:
- Create use case implementation
- Create custom hooks that consume use cases
- Setup Zustand store for feature state
- Implement error handling and loading states

### Step 5: Generate Infrastructure Layer
- Implement repository concrete classes
- Setup API clients with proper typing
- Create adapters for external services
- Configure error handling and retries

### Step 6: Generate Presentation Layer
- Create feature-specific components
- Setup routing for feature pages
- Implement accessibility features
- Add loading and error states

### Step 7: Generate Tests
- Unit tests for domain entities and services
- Integration tests for use cases
- Component tests for presentation layer
- API integration tests for infrastructure layer

## Completion Criteria
- All layers properly implemented
- Clean Architecture dependencies respected
- TypeScript compilation successful
- All tests passing
- Feature integrated with main application