# Selection Sort

A Python module implementing the Selection Sort algorithm.

## Overview

Selection Sort works by repeatedly finding the minimum element from the unsorted portion and placing it at the beginning.

## Installation

```bash
pip install .
```

## Usage

```python
from selection_sort import SelectionSort

sorter = SelectionSort()
result = sorter.sort([64, 25, 12, 22, 11])
print(result)  # [11, 12, 22, 25, 64]
```

## Algorithm Characteristics

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Stable:** No
- **In-place:** Yes

## How It Works

1. Find minimum in unsorted array
2. Swap with first unsorted element
3. Move boundary of sorted portion
4. Repeat until sorted

## License

MIT

---

## CI Status

All PRs are checked for:
- ✅ Syntax (Python, JS, TS, YAML, JSON, Dockerfile, Shell)
- ✅ Secrets (No hardcoded credentials)
- ✅ Security (High-severity vulnerabilities)

