# DH Workspace

A scalable monorepo template for digital humanities projects.

## What is This Workspace?

Given the special needs of coordinating research and digital components, this workspace demonstrates how to structure digital humanities projects using modern project management practices. Under each project, it contains three layers:

- **Research materials** (documents, notes, outputs)
- **Data** (raw and processed)
- **Code** (applications and libraries)

All organized in a way that is:

- Reproducible
- Maintainable
- Scalable
- AI-friendly

---

## Intended Uses

- To teach beginning students in DH a way to organize their research projects
- To be easily used and adapted for DH researchers

## Workspace Structure

```
dh_workspace/
├── .git/                       # Git version control
├── .gitignore                  # Files to ignore in git
├── README.md                   # This file - workspace documentation
│
├── agent_docs/                 # Documentation for AI agents working in this workspace
│   └── rules/                  # Rules that AI agents must follow
│       └── general.md          # General workspace rules (orchestration, data integrity, etc.)
│
├── docs/                       # Workspace wide human-readable documentation
│
└── projects/                   # Container for all research projects (scalable to multiple projects)
    ├── templates/              # Templates
    │   └── project_template/   # Template folder structure and files for new projects
    │
    └── first_project/          # Example project (replace with your project name)
        │
        ├── research/           # Research layer - all research-related documents
        │   ├── design/         # Project design and planning
        │   │   └── design_doc.md       # Research questions, methodology, timeline
        │   ├── journal/        # Research journal - track daily progress
        │   │   └── journal_template.md # For research journal entries
        │   ├── drafts/         # Working drafts of papers and analyses
        │   ├── outputs/        # Final outputs (papers, visualizations, reports)
        │   └── references/     # Bibliography, literature, reference materials
        │
        ├── data/               # Data layer - all project data
        │   ├── raw/            # Original, unmodified data (NEVER edit these!)
        │   └── processed/      # Cleaned and processed data ready for analysis
        │
        └── code/               # Code layer - all technical implementation
            ├── README.md       # Code-specific documentation
            ├── apps/           # Standalone applications (web apps, tools, pipelines)
            └── libs/           # Reusable libraries and utility functions
```

---

## Key Concepts

### Monorepo Within Monorepo

This workspace uses a **monorepo within monorepo** structure:

1. **Outer monorepo** (this workspace): Contains multiple research projects
2. **Inner monorepo** (each project's `code/` folder): Contains apps and libraries for that project

### Three-Layer Architecture

Each project has three interconnected layers:

1. **Research Layer** (`research/`): Design documents, journals, drafts, outputs, references
2. **Data Layer** (`data/`): Raw data and processed data
3. **Code Layer** (`code/`): Applications and libraries

---

## Getting Started

### For Users

1. Navigate to `projects/first_project/`
2. Read [research/design/design_doc.md](research/design/design_doc.md) to understand project planning
3. Start your research journal in [research/journal/research_journal.md](research/journal/research_journal.md)

### For AI Collaboration

1. Check `agent_docs/rules/` for workspace rules. Do note that different terminal agents have different locations for project-specific rules and memory.
2. Understand the project structure before making changes
3. Always maintain the three-layer architecture

---

## Quick Start Guide

### 1. Set Up Your Project

```bash
cd projects/first_project
```

### 2. Fill Out Your Design Document

Edit [research/design/design_doc.md](projects/first_project/research/design/design_doc.md) with your research plan.

### 3. Start Your Research Journal

Use [research/journal/research_journal.md](projects/first_project/research/journal/research_journal.md) as a template.

### 4. Organize Your Data

- Put original data in [data/raw/](projects/first_project/data/raw/)
- Put processed data in [data/processed/](projects/first_project/data/processed/)

### 5. Develop Your Code

- Put applications in [code/apps/](projects/first_project/code/apps/)
- Put reusable libraries in [code/libs/](projects/first_project/code/libs/)

---

## Project Guidelines

### Research Layer

- **design/**: Project design and planning documents
- **journal/**: Daily research journal entries
- **drafts/**: Working drafts of papers and analyses
- **outputs/**: Final outputs (papers, visualizations, etc.)
- **references/**: Bibliography and reference materials

### Data Layer

- **raw/**: Original, unmodified data
- **processed/**: Cleaned and processed data ready for analysis

### Code Layer

- **apps/**: Standalone applications
- **libs/**: Reusable libraries and modules

For the code layer, it's recommended you use a monorepo structure either at the root, or under the `code` with a repo manager of your choice such as NPM7+ or PNPM.

### Utility Layer

- **templates/**: Templates for new projects, etc.
- **playgrounds/**: Playgrounds for testing code, etc.

---

## Adding New Projects

To add a new project: copy [templates/project_template/](templates/project_template/) to `projects/` and rename it to your new project name.

## Resources

- **Agent Rules:** `agent_docs/rules/general.md`

---

## Creator

Bo An
