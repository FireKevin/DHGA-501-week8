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
├── web/
├── desktop/
└── cli/
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
