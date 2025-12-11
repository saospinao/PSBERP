# Create Application Use Case

## Purpose
Create an application use case following hexagonal architecture with ports, adapters, and dependency injection.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - use_case_name
  - service_name
  - input_data
  - output_data
optional_params:
  - external_dependencies
  - business_rules
  - error_scenarios
```

## Task Execution

### Step 1: Elicit Use Case Requirements
Ask user for:

**Use Case Name**: What is the use case name? (use kebab-case, e.g., create-quote)
**Service Name**: Which bounded context does this use case belong to?
**Input Data**: What data does this use case receive? (DTOs, commands)
**Output Data**: What data does this use case return? (response DTOs, events)
**External Dependencies**: What repositories/services does it need? (optional)
**Business Rules**: What business rules must be enforced? (optional)
**Error Scenarios**: What error conditions should be handled? (optional)

### Step 2: Generate Use Case Structure
Create the following files:

```
src/modules/{service-name}/application/
├── use-cases/
│   └── {use-case-name}.use-case.ts
├── commands/
│   └── {use-case-name}.command.ts
├── queries/
│   └── {use-case-name}.query.ts
├── dto/
│   ├── {use-case-name}.dto.ts
│   └── {use-case-name}.response.dto.ts
└── ports/
    ├── repositories/
    │   └── {entity}.repository.interface.ts
    └── services/
        └── {external-service}.interface.ts
```

### Step 3: Create Command/Query Objects
Generate input objects with:
- Property validation decorators
- Type safety with TypeScript
- Documentation with Swagger decorators
- Immutable data structures

Example Command:
```typescript
export class Create{Entity}Command {{
  @IsString()
  @IsNotEmpty()
  readonly property: string;

  @IsOptional()
  @IsUUID()
  readonly optionalId?: string;
}}
```

### Step 4: Create Use Case Implementation
Generate use case with:
- Dependency injection decorators
- Input validation
- Business logic orchestration
- Error handling
- Transaction management
- Domain event handling

Example Use Case:
```typescript
@Injectable()
export class Create{Entity}UseCase {{
  constructor(
    @Inject('{Entity}_REPOSITORY')
    private readonly {entity}Repository: {Entity}RepositoryInterface,
    @Inject('EVENT_BUS')
    private readonly eventBus: EventBusInterface,
  ) {{}}

  async execute(command: Create{Entity}Command): Promise<{Entity}ResponseDto> {{
    // Validation
    // Business logic
    // Repository operations
    // Event publishing
    // Response mapping
  }}
}}
```

### Step 5: Create Repository Interface (Port)
Define repository contract:
- Method signatures for data operations
- Return types with domain entities
- Query parameters and filters
- Error handling contracts

### Step 6: Create Response DTOs
Generate output objects:
- Serialization decorators
- API documentation
- Type transformations
- Nested object handling

### Step 7: Generate Tests
Create comprehensive test suite:
- Unit tests with mocked dependencies
- Integration tests with test database
- Error scenario testing
- Performance testing for complex operations
- Contract testing for external dependencies

### Step 8: Configure Dependency Injection
Update module configuration:
- Provider registration
- Interface-to-implementation binding
- Scope management (singleton, request)
- Circular dependency resolution

## Completion Criteria
- Use case follows hexagonal architecture
- Dependencies properly injected
- Input/output properly validated
- Business rules enforced
- Error handling comprehensive
- Tests cover all scenarios
- Documentation complete