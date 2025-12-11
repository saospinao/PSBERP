# /create-doc Task

When this command is used, execute the following task:

<!-- Powered by BMAD™ Core -->

# Create Document from Template (YAML Driven)

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete documents cannot be created without following this workflow

**VIOLATION INDICATOR:** If you create a complete document without user interaction, you have violated this workflow.

## Critical: Template Discovery

If a YAML Template has not been provided, list all templates from .bmad-core/templates or ask the user to provide another.

## CRITICAL: Title Preservation Rule

**MANDATORY REQUIREMENTS FOR ALL SECTION TITLES:**

1. **Preserve exact title text** - Copy section titles character-by-character from the YAML template
2. **NO NUMBERS** - Never add numeric prefixes (1., 2., 3., etc.) to section titles
3. **ENGLISH ONLY** - Never translate section titles to other languages
4. **NO MODIFICATIONS** - Do not rephrase, reword, or alter section titles in any way
5. **Template is the source of truth** - The title field in the YAML template is definitive

**Examples:**
- ✅ CORRECT: `# High Level Architecture`
- ❌ WRONG: `# 2. High Level Architecture`
- ❌ WRONG: `# Arquitectura de Alto Nivel`
- ❌ WRONG: `# High-Level Architecture Overview`
- ❌ WRONG: `# 2. Arquitectura de Alto Nivel`

**This rule applies to:**
- Main section headings (# Title)
- Subsection headings (## Title)
- All levels of nested sections

**VIOLATION INDICATOR:** If you add numbers, translate, or modify any section title from the template, you have violated this rule.

## CRITICAL: Document Language Rule

**ALL DOCUMENT CONTENT MUST BE WRITTEN IN ENGLISH:**

Regardless of what language you use to converse with the user, ALL documentation artifacts must be written entirely in English.

**This applies to:**
- Section titles (already covered by Title Preservation Rule)
- Section content and descriptions
- Examples and code comments
- Table contents and headers
- Bullet points and numbered lists
- Technical specifications
- User stories and acceptance criteria
- All other documentation text

**Examples:**
- ✅ CORRECT: "The system must support user authentication"
- ❌ WRONG: "El sistema debe soportar autenticación de usuarios"
- ✅ CORRECT: "Epic 1: Foundation and Infrastructure"
- ❌ WRONG: "Epic 1: Fundación e Infraestructura"

**IMPORTANT DISTINCTION:**
- **Conversation with user:** Use user's preferred language (Spanish, English, etc.)
- **Document content:** ALWAYS English, no exceptions

**VIOLATION INDICATOR:** If any document content (titles, descriptions, examples, etc.) is written in a language other than English, you have violated this rule.

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present section content
2. Provide detailed rationale (explain trade-offs, assumptions, decisions made)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next section"
   - **Options 2-9:** Select 8 methods from data/elicitation-methods
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

**NEVER ask yes/no questions or use any other format.**

## Processing Flow

1. **Parse YAML template** - Load template metadata and sections
2. **Set preferences** - Show current mode (Interactive or YOLO), confirm output file
3. **If YOLO mode:**
   - Count total sections
   - Estimate optimal batch count based on section complexity
   - Split document into 3-4 batches (~12-17 sections each)
   - Process each batch → Save → STOP → Wait for "continue"
   - Repeat until all batches complete

4. **If Interactive mode:**
   - Process each section one at a time:
     - Skip if condition unmet
     - Check agent permissions (owner/editors)
     - **PRESERVE EXACT TITLE from template (no numbers, no translation)**
     - Draft content using section instruction
     - Present content + detailed rationale
     - **IF elicit: true** → MANDATORY 1-9 options format
     - Save to file after section
     - Wait for user response before next section

5. **Continue until all sections complete**

## Detailed Rationale Requirements

When presenting section content, ALWAYS include rationale that explains:

- Trade-offs and choices made (what was chosen over alternatives and why)
- Key assumptions made during drafting
- Interesting or questionable decisions that need user attention
- Areas that might need validation

## Elicitation Results Flow

After user selects elicitation method (2-9):

1. Execute method from data/elicitation-methods
2. Present results with insights
3. Offer options:
   - **1. Apply changes and update section**
   - **2. Return to elicitation menu**
   - **3. Ask any questions or engage further with this elicitation**

## Agent Permissions

When processing sections with agent permission fields:

- **owner**: Note which agent role initially creates/populates the section
- **editors**: List agent roles allowed to modify the section
- **readonly**: Mark sections that cannot be modified after creation

**For sections with restricted access:**

- Include a note in the generated document indicating the responsible agent
- Example: "_(This section is owned by dev-agent and can only be modified by dev-agent)_"

## YOLO Mode

User can type `#yolo` to toggle to YOLO mode (process sections in batches without elicitation).

**MANDATORY BATCH WORKFLOW:**

1. **Automatic batch calculation:**
   - Estimate: `sections × 600 tokens`
   - Max per batch: **22,000 tokens** (safe 10K buffer - Claude can't measure in real-time)
   - Batches needed: `total_estimate ÷ 22,000` (rounded up)
   - If complex sections detected: multiply estimate × 1.5

2. **CRITICAL - Repeatable sections (epics, stories, etc.):**
   - Count total repeatable items (e.g., 10 epics × 10 stories each)
   - Estimate tokens per item: `epic ~7,000 tokens`, `story ~800 tokens`
   - Calculate: `items × tokens_per_item = total_tokens`
   - If `total_tokens > 22,000`: Split into sub-batches
   - Example: 10 epics × 7K = 70K tokens → 4 sub-batches (3-3-2-2 epics)
   - Process each sub-batch separately with pauses

3. **Process EACH batch:**
   - **PRESERVE EXACT TITLES from template (no numbers, no translation)**
   - Generate content for batch sections
   - Save to file
   - STOP and tell user: "✅ Batch X/Y complete: Sections A-B saved. Type 'continue'."
   - WAIT for user to type "continue"
   - Repeat until all batches complete

**Examples:**
- 30 sections (~18K tokens) → 1 batch (0 pauses)
- 50 sections (~30K tokens) → 2 batches (1 pause)
- 50 sections + 10 epics (~80K tokens) → 4 batches (3 pauses)

**THIS IS NON-NEGOTIABLE FOR YOLO MODE**

## CRITICAL REMINDERS

**❌ NEVER:**

- Ask yes/no questions for elicitation
- Use any format other than 1-9 numbered options
- Create new elicitation methods
- Add numbers to section titles (1., 2., etc.)
- Translate section titles from English
- Modify or rephrase section titles from the template

**✅ ALWAYS:**

- Use exact 1-9 format when elicit: true
- Select options 2-9 from data/elicitation-methods only
- Provide detailed rationale explaining decisions
- End with "Select 1-9 or just type your question/feedback:"
- Preserve exact section titles from YAML template without modification
- Keep all section titles in English as defined in template
