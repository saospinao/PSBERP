# Scaffold Backend Microservice

## Purpose
Generate complete microservice structure with Clean Architecture + DDD principles using .NET 10.

**CRITICAL**: Always use .NET 10 with C# and Entity Framework Core. Follow Clean Architecture patterns strictly. No raw SQL allowed - use EF Core for all database operations.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - service_name
  - domain_contexts
optional_params:
  - database_type
  - messaging_transport
  - shared_libraries
```

## Task Execution

### Step 1: Elicit Service Requirements
Ask user for the following information:

**Service Name**: What would you like to name your microservice? (use kebab-case)
**Domain Contexts**: List the main bounded contexts for this service (e.g., quotes, products, billing)
**Database Type**: Which database will this service use? (PostgreSQL, MySQL, MongoDB - default: PostgreSQL)
**Messaging Transport**: What messaging transport? (Redis, RabbitMQ, gRPC - default: Redis)
**Shared Libraries**: Any existing shared libraries to include? (optional)

### Step 2: Generate MonoRepo Structure
Create the following Nx workspace structure:

```
apps/{service-name}/
├── src/
│   ├── modules/
│   │   └── {context}/
│   │       ├── application/
│   │       │   ├── ports/
│   │       │   ├── use-cases/
│   │       │   ├── commands/
│   │       │   ├── queries/
│   │       │   └── dto/
│   │       ├── domain/
│   │       │   ├── entities/
│   │       │   ├── value-objects/
│   │       │   ├── aggregates/
│   │       │   ├── events/
│   │       │   └── services/
│   │       └── infrastructure/
│   │           ├── repositories/
│   │           ├── services/
│   │           └── events/
│   ├── api/
│   │   ├── controllers/
│   │   ├── guards/
│   │   ├── middlewares/
│   │   └── filters/
│   ├── config/
│   ├── main.ts
│   └── app.module.ts
├── test/
├── Microservicio.Infrastructure/
│   ├── Persistence/
│   │   ├── EF/
│   │   │   ├── DbContexts/
│   │   │   └── Migrations/
│   └── migrations/
└── package.json
```

### Step 3: Setup .NET Configuration
- Initialize .NET 10 solution and projects
- Configure C# language features
- Configure Nx workspace if not exists
- Setup Entity Framework Core with selected database provider
- Configure dependency injection container
- Setup validation with class-validator
- Configure Swagger/OpenAPI documentation
- Setup health checks and monitoring

### Step 4: Generate Domain Contexts
For each bounded context:
- Create hexagonal architecture layers
- Generate base domain entities with DDD patterns
- Create application ports (interfaces)
- Setup infrastructure adapters
- Create Entity Framework Core entity configurations
- Generate initial use cases

### Step 5: Setup Shared Infrastructure
- Configure JWT authentication
- Setup Redis for caching and messaging
- Configure CORS and security headers
- Setup logging with Winston
- Configure environment variables
- Setup database connection pooling

### Step 6: Generate Initial Tests
- Unit tests for domain entities
- Integration tests for use cases
- E2E tests for API endpoints
- Repository tests with test database
- Mocking strategies for external dependencies

## Completion Criteria
- MonoRepo structure follows hexagonal architecture
- All dependencies properly configured
- Entity Framework Core migrations generated and applied
- TypeScript compiles without errors
- Initial tests pass
- Swagger documentation accessible
- Health checks responding