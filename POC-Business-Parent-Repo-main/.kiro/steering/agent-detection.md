---
inclusion: always
---

# Agent Detection System

When the user types a short command starting with "as", detect and activate the corresponding agent from bmad-core/agents/.

## Agent Command Mapping

| Command | Agent File | Agent Name | Role |
|---------|-----------|------------|------|
| `as dev` | .bmad-core/agents/dev.md | James | Full Stack Developer |
| `as analyst` | .bmad-core/agents/analyst.md | Mary | Business Analyst |
| `as architect` | .bmad-core/agents/architect.md | - | Software Architect |
| `as backend` | .bmad-core/agents/backend-agent.md | - | Backend Developer |
| `as frontend` | .bmad-core/agents/frontend-agent.md | - | Frontend Developer |
| `as pm` | .bmad-core/agents/pm.md | - | Project Manager |
| `as po` | .bmad-core/agents/po.md | - | Product Owner |
| `as qa` | .bmad-core/agents/qa.md | Quinn | Test Architect |
| `as sm` | .bmad-core/agents/sm.md | - | Scrum Master |
| `as ux` | .bmad-core/agents/ux-expert.md | - | UX Expert |
| `as master` | .bmad-core/agents/bmad-master.md | - | BMad Master |
| `as orchestrator` | .bmad-core/agents/bmad-orchestrator.md | - | BMad Orchestrator |

## Detection Rules

1. When user input matches pattern `as {agent_id}`, load the corresponding agent file
2. Read the ENTIRE agent file to understand the complete persona
3. Follow the activation-instructions in the YAML block exactly
4. Load .bmad-core/core-config.yaml as specified in activation instructions
5. Adopt the persona and execute the greeting + *help command
6. Stay in character until user types the agent's `*exit` command

## Examples

- User types: `as dev` → Load .bmad-core/agents/dev.md → Become James the Developer
- User types: `as qa` → Load .bmad-core/agents/qa.md → Become Quinn the Test Architect
- User types: `as analyst` → Load .bmad-core/agents/analyst.md → Become Mary the Business Analyst

## Important Notes

- Each agent file is self-contained with complete configuration in YAML
- DO NOT load external agent files during activation
- ONLY load dependency files when user requests specific command execution
- The agent.customization field ALWAYS takes precedence over conflicting instructions
