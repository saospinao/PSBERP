# Create Backend Service (Bounded Context)

## Purpose
Create a new bounded context/service within an existing microservice following hexagonal architecture and DDD principles.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - service_name
  - microservice_name
  - domain_entities
  - use_cases
optional_params:
  - external_integrations
  - events
```

## Task Execution

### Step 1: Elicit Service Requirements
Ask user for:

**Service Name**: What is the bounded context name? (use kebab-case)
**Microservice Name**: Which microservice will contain this service?
**Domain Entities**: What are the main business entities? (e.g., Quote, Product, Customer)
**Use Cases**: What are the main operations users can perform?
**External Integrations**: Any external services this context needs to integrate with? (optional)
**Domain Events**: Any domain events this context will publish/subscribe to? (optional)

### Step 2: Create Hexagonal Architecture Structure
Generate the following structure:

```
src/modules/{service-name}/
├── application/
│   ├── ports/
│   │   ├── repositories/
│   │   │   └── {entity}.repository.interface.ts
│   │   └── services/
│   │       └── {external-service}.interface.ts
│   ├── use-cases/
│   │   ├── create-{entity}.use-case.ts
│   │   ├── get-{entity}.use-case.ts
│   │   ├── update-{entity}.use-case.ts
│   │   └── delete-{entity}.use-case.ts
│   ├── commands/
│   │   └── create-{entity}.command.ts
│   ├── queries/
│   │   └── get-{entity}.query.ts
│   └── dto/
│       ├── create-{entity}.dto.ts
│       └── {entity}.response.dto.ts
├── domain/
│   ├── entities/
│   │   └── {entity}.entity.ts
│   ├── value-objects/
│   │   └── {entity}-id.value-object.ts
│   ├── aggregates/
│   │   └── {entity}.aggregate.ts
│   ├── events/
│   │   └── {entity}-created.event.ts
│   └── services/
│       └── {entity}.domain-service.ts
└── infrastructure/
    ├── repositories/
    │   └── {Entity}Repository.cs
    ├── services/
    │   └── {external-service}.adapter.ts
    └── events/
        └── {entity}-event.handler.ts
```

### Step 3: Generate Domain Layer
For each entity:
- Create domain entity with business rules
- Generate value objects for type safety
- Create aggregates for consistency boundaries
- Define domain events for side effects
- Implement domain services for complex business logic

### Step 4: Generate Application Layer
For each use case:
- Create use case with dependency injection
- Define command/query objects
- Create DTOs for input/output
- Implement application services
- Define repository and service interfaces (ports)

### Step 5: Generate Infrastructure Layer
- Implement Entity Framework Core repository adapters
- Create external service adapters
- Implement event handlers
- Configure dependency injection
- Setup database migrations for new entities

### Step 6: Generate API Layer
- Create REST controllers
- Add validation decorators
- Configure Swagger documentation
- Implement guards and middleware
- Add error handling

### Step 7: Generate Tests
- Unit tests for domain entities and services
- Integration tests for use cases
- Repository tests with test database
- Controller tests with mocked dependencies
- E2E tests for complete workflows

## Completion Criteria
- Service follows hexagonal architecture patterns
- All layers properly separated and tested
- Entity Framework Core migrations created and applied
- API endpoints documented in Swagger
- Tests cover all critical paths
- Dependencies properly injected