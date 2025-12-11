<!-- Powered by BMAD™ Core -->

# User-Defined Preferred Patterns and Preferences

## Backend Preferences (.NET 10)

### Framework & Language
- **MANDATORY**: .NET 10 with C# Minimal API
- **API Style**: Minimal API (lightweight, modern approach)
- **NO** MVC Controllers - Use Minimal API endpoints only

### Database
- **MANDATORY**: PostgreSQL for all microservices
- **ORM**: Entity Framework Core 10 (primary - matches .NET 10 version)
- **LINQ Extensions**: linq2db, DynamicLinq, LinqKit for advanced queries
- **Primary Keys**: UUID (Guid) for ALL entities - NO exceptions
- **Migrations**: EF Core 10 Migrations for schema version control
- **DateTime Types**: 
  - **MANDATORY**: Use `DateTimeOffset` for ALL timestamp fields (CreatedAt, UpdatedAt, etc.)
  - **FORBIDDEN**: NEVER use `DateTime` for timestamp fields in entities or DTOs
  - **Rationale**: PostgreSQL uses TIMESTAMP WITH TIME ZONE which maps to DateTimeOffset
  - **Date Only**: Use `DateOnly` for date-only fields (BirthDate, ExpenseDate)
  - **Time Only**: Use `TimeOnly` for time-only fields (OpeningTime, ClosingTime)

### Validation
- **MANDATORY**: FluentValidation for all DTOs and commands

### API Documentation
- **MANDATORY**: Scalar for API documentation
- **FORBIDDEN**: Do NOT use Swagger/Swashbuckle

### Architecture
- **Pattern**: Clean Architecture + DDD
- **Microservices**: Each service with independent PostgreSQL database
- **No Shared Databases**: Services communicate via APIs or events
- **CQRS**: Command/Query separation in Application layer

### Testing
- **Framework**: xUnit (MANDATORY)
- **TDD**: Test-Driven Development approach required
- **Unit Tests**: EF Core InMemory for fast tests
- **Integration Tests**: PostgreSQL Test Containers for real scenarios
- **Coverage**: Aim for >80% code coverage

### PDF Generation
- **Library**: QuestPDF for document generation
- **Testing**: Snapshot/output validation for PDF tests

### Code Quality
- **Analyzers**: Enable .NET code analyzers
- **Format**: Use `dotnet format` for code style
- **EditorConfig**: Enforce coding standards

### Localization
- **i18n/l10n**: Built-in .NET localization support
- **Resources**: Use .resx files for translations

### Development Environment
- **Local Development**: Direct execution with `dotnet run`
- **PostgreSQL Local**: Use local PostgreSQL instance or cloud dev DB

### Production Deployment
- **Containerization**: Docker for production deployments
- **Orchestration**: Kubernetes or Docker Compose
- **Each Service**: Independent container with health checks

## Frontend Preferences (Next.js 16)

### Framework
- **Default**: Next.js 16 with TypeScript and App Router
- **Exception**: Pure React + Vite only for offline-first scenarios

### State Management
- **Zustand**: Preferred for global state

### UI Components
- **shadcn/ui**: Component library
- **Radix UI**: Primitives
- **TailwindCSS v4**: Styling

### Testing
- **Vitest**: Test runner
- **React Testing Library**: Component testing
- **MSW**: API mocking

### Validation
- **Zod**: Schema validation
- **React Hook Form**: Form management

## Cross-Stack Preferences

### Communication
- **REST API**: Primary communication protocol
- **gRPC**: For high-performance inter-service calls
- **Message Broker**: RabbitMQ or Azure Service Bus for async events

### Security
- **Authentication**: JWT tokens
- **Authorization**: Role-based access control
- **HTTPS**: Mandatory for all environments

### Logging & Monitoring
- **Structured Logging**: Use ILogger in .NET
- **Correlation IDs**: Track requests across services
- **Health Checks**: Implement health endpoints for all services

### Error Handling
- **Problem Details**: RFC 7807 for error responses
- **Global Exception Handler**: Middleware for centralized error handling
- **Validation Errors**: Return 400 with detailed validation messages
