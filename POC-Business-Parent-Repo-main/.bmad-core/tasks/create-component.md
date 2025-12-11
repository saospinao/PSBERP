# Create UI Component

## Purpose
Create a React component with TypeScript, accessibility features, and comprehensive tests.

## Task Configuration
```yaml
elicit: true
interactive: true
required_params:
  - component_name
  - feature
  - component_type
optional_params:
  - props
  - accessibility_level
```

## Task Execution

### Step 1: Elicit Component Requirements
Ask user for:

**Component Name**: What should the component be called? (use PascalCase)
**Feature**: Which feature does this component belong to?
**Component Type**: What type of component is this?
- page: Full page component with routing
- container: Logic container that manages state
- presentation: Pure presentation component
- form: Form component with validation
- layout: Layout wrapper component

**Props**: What props should this component accept? (optional)
**Accessibility Level**: What accessibility level is needed?
- basic: Basic ARIA labels and keyboard support
- enhanced: Enhanced navigation and screen reader support
- wcag-aa: Full WCAG 2.1 AA compliance

### Step 2: Generate Component File
Create component with:
- TypeScript interface for props
- Proper React.memo for performance
- Forward refs if needed
- Default props and prop validation

### Step 3: Implement Accessibility Features
Based on accessibility level:
- Add proper ARIA attributes
- Implement keyboard navigation
- Ensure proper color contrast
- Add screen reader support
- Include focus management

### Step 4: Add Styling
- Use TailwindCSS for styling
- Follow design system patterns
- Implement responsive design
- Add hover/focus states
- Support theme variations

### Step 5: Generate Tests
Create comprehensive test suite:
- Unit tests for component behavior
- Accessibility tests (using jest-axe)
- User interaction tests
- Visual regression tests if needed
- Performance tests for complex components

### Step 6: Generate Documentation
- Add JSDoc comments
- Create Storybook stories if configured
- Document props and usage examples
- Add accessibility notes

## Component Template Structure
```typescript
interface {ComponentName}Props {
  // Props definition with proper typing
  className?: string;
  'data-testid'?: string;
}

export const {ComponentName} = memo<{ComponentName}Props>(({
  className,
  'data-testid': testId = '{component-name}'
}) => {
  // Component implementation
  return (
    <div className={cn('component-base-styles', className)} data-testid={testId}>
      {/* Component content */}
    </div>
  );
});

{ComponentName}.displayName = '{ComponentName}';
```

## Completion Criteria
- Component follows TypeScript best practices
- Accessibility requirements met
- Comprehensive test coverage
- Proper styling and responsive design
- Documentation complete