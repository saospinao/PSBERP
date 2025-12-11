# Frontend Development Standards

## Architecture Principles

### Clean Architecture Implementation
- **Domain Layer**: Business entities, value objects, and business rules only
- **Application Layer**: Use cases, custom hooks, and state management
- **Infrastructure Layer**: API clients, repositories implementations, external service adapters
- **Presentation Layer**: React components, pages, and UI logic only

### Dependency Rules
- Inner layers must not know about outer layers
- Dependencies point inward (from outer to inner layers)
- Use dependency inversion for external concerns

## Technology Stack Standards

### Core Technologies
- **Next.js**: 14+ with App Router and TypeScript
- **React**: 18+ with functional components and hooks (via Next.js)
- **TypeScript**: Strict mode enabled, no `any` types
- **TailwindCSS**: Utility-first CSS framework
- **Shadcn/ui + Radix UI**: Component library foundation

### Framework Selection Rules
- **Default**: Always use Next.js 16+ with App Router
- **Exception**: Only use pure React + Vite when user specifically requests offline-first functionality
- **Reasoning**: Next.js provides better DX, built-in optimization, and easier deployment while maintaining PWA capabilities

### State Management
- **Zustand**: Primary state management solution
- Feature-based stores following DDD patterns
- Global state only for truly global concerns
- Local state for component-specific needs

### Development Tools
- **Next.js**: Built-in build system and development server
- **Vitest**: Unit and integration testing (configured with Next.js)
- **React Testing Library**: Component testing
- **MSW**: API mocking for tests
- **ESLint + Prettier**: Code quality and formatting (Next.js config)

## MCP Component Strategy
- **Always First**: Check MCP Shadcn registry before creating any component
- **Execute MCP**: Actively run MCP commands to search and install components
- **Workflow**: For buttons, forms, inputs, cards, dialogs, tables → Execute "Show me [type] components from shadcn registry" → Then execute "Add the [name] component to my project"
- **Error Reduction**: 90% fewer bugs using MCP vs manual creation

## Component Standards

### Component Structure
```typescript
interface ComponentProps {
  // Required props
  children: React.ReactNode;
  // Optional props with defaults
  className?: string;
  variant?: 'default' | 'secondary';
  'data-testid'?: string;
}

export const Component = memo<ComponentProps>(({
  children,
  className,
  variant = 'default',
  'data-testid': testId = 'component'
}) => {
  // Component implementation
  return (
    <div className={cn(baseStyles, variantStyles[variant], className)} data-testid={testId}>
      {children}
    </div>
  );
});

Component.displayName = 'Component';
```

### Component Naming
- **PascalCase** for component names
- **kebab-case** for file names and data-testid attributes
- **camelCase** for props and functions
- Descriptive names that indicate purpose

### Props Guidelines
- Always define TypeScript interfaces for props
- Use optional props with sensible defaults
- Include className for style overrides
- Add data-testid for testing
- Document complex props with JSDoc

## State Management Patterns

### Zustand Store Structure
```typescript
interface FeatureState {
  // Domain entities
  entities: Entity[];
  selectedEntity: Entity | null;
  
  // UI state
  loading: boolean;
  error: string | null;
  
  // Actions (use case calls)
  loadEntities: () => Promise<void>;
  selectEntity: (id: string) => void;
  updateEntity: (entity: Entity) => Promise<void>;
  clearError: () => void;
}

export const useFeatureStore = create<FeatureState>()(
  devtools(
    (set, get) => ({
      // Initial state
      entities: [],
      selectedEntity: null,
      loading: false,
      error: null,
      
      // Actions implementation
      loadEntities: async () => {
        set({ loading: true, error: null });
        try {
          const entities = await loadEntitiesUseCase.execute();
          set({ entities, loading: false });
        } catch (error) {
          set({ error: error.message, loading: false });
        }
      },
      
      // Other actions...
    }),
    { name: 'featureStore' }
  )
);
```

## Testing Standards

### Testing Strategy
- **Unit Tests**: Domain entities, use cases, utilities
- **Integration Tests**: Feature workflows, API integration
- **Component Tests**: User interactions, accessibility
- **E2E Tests**: Critical user journeys (minimal)

### Test Structure
```typescript
describe('ComponentName', () => {
  it('should render correctly with default props', () => {
    render(<ComponentName>Test content</ComponentName>);
    expect(screen.getByTestId('component-name')).toBeInTheDocument();
  });
  
  it('should handle user interactions', async () => {
    const handleClick = jest.fn();
    render(<ComponentName onClick={handleClick} />);
    
    await user.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalled();
  });
  
  it('should be accessible', async () => {
    const { container } = render(<ComponentName />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
```

## Accessibility Standards

### WCAG 2.1 AA Compliance
- Semantic HTML elements
- Proper heading hierarchy
- Keyboard navigation support
- Screen reader compatibility
- Color contrast minimum 4.5:1

### ARIA Implementation
- Use semantic HTML first, ARIA second
- Proper labeling with aria-label or aria-labelledby
- Role attributes for custom components
- State communication with aria-expanded, aria-selected
- Live regions for dynamic content updates

## Performance Standards

### Bundle Optimization
- Code splitting by route and feature
- Lazy loading for non-critical components
- Tree shaking for unused code
- Bundle size budget: 500KB total

### Runtime Performance
- React.memo for expensive components
- useMemo for expensive calculations
- useCallback for event handlers passed to children
- Virtual scrolling for large lists

### Loading Performance
- Image optimization and lazy loading
- Progressive loading strategies
- Skeleton screens for loading states
- Prefetch critical resources

## Security Guidelines

### Client-Side Security
- No API keys or secrets in frontend code
- Input validation and sanitization
- XSS prevention measures
- Secure handling of user data

### Authentication
- Token-based authentication (JWT)
- Secure token storage
- Automatic token refresh
- Proper logout handling

## File Organization

### Feature Structure
```
src/
├── modules/
│   ├── sales/                    # MODULE
│   │   ├── quotes/              # DOMAIN
│   │   │   ├── cart/            # FEATURE
│   │   │   │   ├── domain/
│   │   │   │   │   ├── entities/
│   │   │   │   │   ├── repositories/     # Interfaces
│   │   │   │   │   ├── services/         # Domain services
│   │   │   │   │   └── types/
│   │   │   │   ├── application/
│   │   │   │   │   ├── use-cases/
│   │   │   │   │   ├── hooks/            # Custom hooks
│   │   │   │   │   └── store/            # Zustand store
│   │   │   │   ├── infrastructure/
│   │   │   │   │   ├── repositories/     # Implementations
│   │   │   │   │   ├── api/
│   │   │   │   │   └── adapters/
│   │   │   │   └── presentation/
│   │   │   │       ├── components/
│   │   │   │       ├── pages/
│   │   │   │       └── styles/
│   │   │   └── products/        # FEATURE
│   │   │       ├── domain/
│   │   │       ├── application/
│   │   │       ├── infrastructure/
│   │   │       └── presentation/
│   │   └── billing/             # DOMAIN
│   │       ├── invoices/        # FEATURE
│   │       └── reports/         # FEATURE
│   ├── inventory/               # MODULE
│   │   ├── products/            # DOMAIN
│   │   │   ├── catalog/         # FEATURE
│   │   │   └── stock/           # FEATURE
│   │   └── warehouses/          # DOMAIN
│   └── users/                   # MODULE
│       └── authentication/      # DOMAIN
│           ├── login/           # FEATURE
│           └── registration/    # FEATURE
├── shared/
│   ├── components/              # Shadcn/ui components
│   │   └── ui/                  # Base UI Kit components from proyecto/components/ui/
│   ├── hooks/
│   ├── utils/
│   ├── types/
│   └── constants/
├── app/
│   ├── store/                   # Global store
│   ├── providers/               # Context providers
│   ├── router/                  # Routing config
│   └── app.tsx
├── infrastructure/
│   ├── api/                     # API configuration
│   ├── storage/                 # IndexedDB, localStorage
│   └── pwa/                     # PWA configuration
├── assets/
│   ├── fonts/                   # Fonts from proyecto/public/fonts/
│   │   ├── SiesaBT-Light.otf
│   │   ├── SiesaBT-Regular.otf
│   │   └── SiesaBT-Bold.otf
│   ├── images/
│   │   └── logos/               # Logos from proyecto/public/images/logos/
│   │       ├── Siesa_Logosimbolo_Azul.svg
│   │       ├── Siesa_Logosimbolo_Blanco.svg
│   │       ├── Siesa_Simbolo_Azul.svg
│   │       └── Siesa_Simbolo_Blanco.svg
│   └── favicon.ico              # Favicon from proyecto/public/favicon.ico
└── styles/
    └── globals.css              # Consolidated styles + Tailwind + WCAG from proyecto/styles/globals.css
```

### Import Organization
```typescript
// External libraries
import React from 'react';
import { create } from 'zustand';

// Internal utilities
import { cn } from '@/lib/utils';

// Types
import type { User } from '../domain/types/User';

// Components
import { Button } from '@/components/ui/button';
```

## Error Handling

### Error Boundaries
- Feature-level error boundaries
- Graceful fallback UI
- Error reporting and logging
- User-friendly error messages

### API Error Handling
- Centralized error handling in HTTP client
- Proper error typing
- User-friendly error messages
- Retry mechanisms for transient errors

## Progressive Web App Standards

### PWA Features
- Service worker for caching and offline support
- Web app manifest for installability
- Push notifications (when needed)
- Background sync capabilities

### Offline Strategy
- Cache-first for static assets
- Network-first for dynamic data
- Fallback pages for offline scenarios
- Sync when connection restored

## Language Standards (Frontend & Backend)

### Spanish for All User-Facing Content (CRITICAL RULE)

**MANDATORY: All text visible to end users MUST be in Spanish.**

#### ✅ Spanish Required:
- UI labels, buttons, forms, messages, notifications
- API responses, validation errors, email templates
- Any text the user sees (frontend or backend)

#### ✅ English Required:
- Code (variables, functions, classes)
- Technical logs, comments, git commits
- Developer documentation

#### ❌ Never mix languages in user-facing text

**Examples:**
```typescript
// ✅ CORRECT
<Button>Guardar</Button>
toast.success("Datos guardados correctamente");
throw new BadRequestException('No se pudo crear el usuario');

// ❌ INCORRECT
<Button>Save cambios</Button>
toast.error("Failed al guardar");
throw new BadRequestException('Invalid datos proporcionados');
```

**Implementation:**
- Create message constants in Spanish
- Validate all user-facing text before story completion
- Technical logs stay in English, user messages in Spanish