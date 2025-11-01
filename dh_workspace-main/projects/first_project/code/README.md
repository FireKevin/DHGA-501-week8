# Code Monorepo

This is the code layer of your digital history project, organized as a monorepo.

---

## Structure

```
code/
├── apps/       # Standalone applications
├── libs/       # Reusable libraries and modules
└── README.md   # This file
```

---

## What Goes Where?

### `apps/` - Applications

Put standalone applications here. Examples:
- Web applications
- Data visualization dashboards
- Analysis tools
- Processing pipelines

Each app should be self-contained and may depend on libraries in `libs/`.

**Example:**
```
apps/
├── web_interface/
├── data_processor/
└── visualization_dashboard/
```

### `libs/` - Libraries

Put reusable code here. Examples:
- Data processing utilities
- Analysis functions
- Helper modules
- Shared configurations

Libraries can be used by multiple apps.

**Example:**
```
libs/
├── data_utils/
├── analysis_tools/
└── visualization_helpers/
```

---

## Technology Stack

This monorepo is **technology-agnostic**. You can use:

- Python (Django, Flask, FastAPI, Jupyter)
- JavaScript/TypeScript (React, Vue, Node.js)
- R (Shiny, analysis scripts)
- Any other language or framework

---

## Getting Started

### 1. Choose Your Technology Stack

Decide what languages and frameworks you'll use.

### 2. Set Up Your Development Environment

Install necessary dependencies:

```bash
# For Python projects
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# For Node.js projects
npm install

# For R projects
# Install packages as needed
```

### 3. Organize Your Code

- Create folders for your apps in `apps/`
- Create folders for shared code in `libs/`
- Keep each module focused and well-documented

---

## Best Practices

### 1. Modularity

- Keep apps independent
- Put shared code in `libs/`
- Avoid tight coupling between modules

### 2. Documentation

- Add README files to each app and library
- Document your functions and classes
- Explain complex logic with comments

### 3. Data Flow

```
../../data/raw/  →  [Your Code]  →  ../../data/processed/
                                   →  ../../research/outputs/
```

- Read data from `../../data/raw/` or `../../data/processed/`
- Write outputs to `../../research/outputs/`
- Never modify raw data

### 4. Version Control

- Commit working code regularly
- Use meaningful commit messages
- Don't commit large binary files or generated outputs

---

## Working with AI

When using AI to generate code:

1. **You are the orchestrator**: Direct the AI, don't let it direct you
2. **Provide context**: Give AI access to your data and requirements
3. **Verify outputs**: Always test AI-generated code
4. **Document decisions**: Note why you made certain choices

---

## Common Patterns

### Pattern 1: Data Processing Pipeline

```
apps/data_pipeline/
├── extract.py    # Load raw data
├── transform.py  # Process and clean
└── load.py       # Save processed data
```

### Pattern 2: Analysis + Visualization

```
apps/analysis/
└── analyze.py

apps/visualization/
└── visualize.py
```

### Pattern 3: Web Application

```
apps/web_app/
├── backend/
├── frontend/
└── api/
```

---

## Dependency Management

### Python

Create `requirements.txt`:
```
pandas==2.0.0
numpy==1.24.0
matplotlib==3.7.0
```

### Node.js

Use `package.json`:
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "axios": "^1.4.0"
  }
}
```

---

## Testing

Consider adding tests:

```
code/
├── apps/
├── libs/
└── tests/
    ├── unit/
    └── integration/
```

---

## Next Steps

1. Choose your technology stack
2. Create your first app or library
3. Start with a simple proof of concept
4. Iterate and expand

---

**Remember:** Good code is maintainable code. Future you (and your collaborators) will thank you for:
- Clear structure
- Good documentation
- Consistent naming
- Version control
