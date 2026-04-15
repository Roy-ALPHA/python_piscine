# Python Piscine

A hands-on Python training repository organized as progressive modules (`module_0` → `module_10`).
Each module focuses on a core topic (fundamentals, OOP, exceptions, streams, packaging, validation, and functional patterns) through small standalone exercises.

## Repository Layout

```text
python_piscine/
├── module_0/   # Python basics (variables, functions, loops, recursion)
├── module_1/   # Functions, factory patterns, basic analytics
├── module_2/   # Error handling and custom exceptions
├── module_3/   # CLI args, tuples, collections, stream-style processing
├── module_4/   # File I/O and resource management
├── module_5/   # Abstraction, protocols, adapters, processing pipelines
├── module_6/   # Imports, packages, circular imports, module paths
├── module_7/   # OOP design patterns in a card-game domain
├── module_8/   # Environments, dependency loading, dotenv config
├── module_9/   # Data validation with Pydantic models
├── module_10/  # Lambda, higher-order functions, functools, decorators
└── README.md
```

## Module-by-Module Overview

### `module_0` — Foundations
- `ex0` to `ex4`: first functions, arithmetic, conditionals, formatted output.
- `ex5`: iterative and recursive counting implementations.
- `ex6` to `ex7`: summary/inventory style exercises.

### `module_1` — Structured Functions & Small Systems
- Garden-themed scripts with typed functions and cleaner `main()` flows.
- Includes object/factory-style exercise (`ft_plant_factory.py`) and analytics-style tasks.
- `subject/en.subject.pdf` contains the assignment statement.

### `module_2` — Exceptions
- `try/except/finally`, explicit `raise`, custom errors.
- Progresses from single error checks to small management scripts.

### `module_3` — Arguments, Data Structures, and Analytics Flows
- Command-line argument processing (`sys.argv`).
- Coordinates/tuples, tracking systems, inventory and stream-like handling.

### `module_4` — Files and Recovery Workflows
- File opening/reading/writing and robust cleanup in `finally` blocks.
- Exercises model archive, vault, and crisis recovery scenarios.

### `module_5` — Abstractions and Pipelines
- Abstract base classes and protocols (`ABC`, `Protocol`).
- Multi-stage processing systems with adapters and centralized managers.

### `module_6` — Imports & Packages
- Import strategies (`import x`, `from x import y`, aliasing).
- Package structure in `alchemy/` with nested subpackages (`grimoire/`, `transmutation/`).
- Circular import and module path exploration scripts.

### `module_7` — OOP Patterns (Card Game)
- Base/derived card classes and enums.
- Composition (`Deck`), interfaces/protocol-like abstractions, strategy/factory patterns.
- Tournament ranking platform in `ex4`.

### `module_8` — Environment & Dependency Management
- `ex0/construct.py`: detect global vs virtual environment.
- `ex1/loading.py`: dynamic imports and dependency checks.
- `ex2/oracle.py`: load configuration from `.env` using `python-dotenv`.

### `module_9` — Validation with Pydantic
- Typed data models with constrained fields and custom validators.
- Examples include space station, alien contact, and crew/mission validation.

### `module_10` — Functional Python
- Lambda expressions, `map/filter/sorted` functional flows.
- Higher-order behavior, scope exercises, `functools`, and decorators.

## Quick Start

### 1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies used in advanced modules
```bash
pip install pydantic python-dotenv numpy pandas matplotlib requests
```

### 3) Run any exercise directly
```bash
python module_0/ex0/ft_hello_garden.py
python module_5/ex0/stream_processor.py
python module_9/ex0/space_station.py
```

## Notes

- Some files intentionally demonstrate failure/error cases as part of the exercises.
- A few filenames contain a leading space (for example in `module_0/ex5` and `module_3/ex1`), so quote paths in shell commands when needed.
- `module_8/ex1` includes both `requirements.txt` and `pyproject.toml` (Poetry-style setup example).

## Suggested Learning Order

Follow modules in numeric order (`module_0` to `module_10`) for the smoothest progression.
