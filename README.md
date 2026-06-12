# Fully Optimized Doubly Linked List (DLL) in Python

A high-performance, production-ready implementation of a Doubly Linked List written in Python. This project transitions standard linear-time $O(N)$ operations down to constant-time $O(1)$ efficiency by maintaining a persistent `tail` pointer alongside the `head` pointer.

## 🚀 Key Features & Architectural Enhancements

- **Dual-Boundary Tracking:** Built-in `head` and `tail` pointers for instant access to both ends of the list.
- **O(1) Boundary Operations:** Insertions and deletions at the absolute front or back run in constant time.
- **High-Performance Backward Traversal:** Printing the list in reverse skips forward loops entirely, walking directly backward from the tail.
- **In-Place List Reversal:** Flips the entire list using minimal variable overhead with optimal space complexity.
- **Advanced Utility Methods:** Includes built-in cycle detection, duplicate filtering, safe index-based operations, and a custom Python iterator.

## 📊 Algorithmic Efficiency Comparison

| Operation | Standard DLL (No Tail) | This Implementation (With Tail) |
| :--- | :--- | :--- |
| `insert_at_start` | $O(1)$ | **$O(1)$** |
| `insert_at_last` | $O(N)$ | **$O(1)$** *(Massive Upgrade)* |
| `delete_first` | $O(1)$ | **$O(1)$** |
| `delete_last` | $O(N)$ | **$O(1)$** *(Massive Upgrade)* |
| `print_backward` | $O(N)$ (Forward + Back) | **$O(N)$** *(50% fewer CPU operations)* |
| `reverse_list` | $O(N)$ | **$O(N)$** *(In-place)* |

## 🛠️ Method Overview

### Structural Operations
- `insert_at_start(item)` / `insert_at_last(item)` — Fast boundary insertions.
- `insert_after(address, item)` / `insert_at_index(index, item)` — Flexible position-based adding.
- `delete_first()` / `delete_last()` — Optimized boundary removals.
- `delete_item(item)` / `delete_at_index(index)` — Precise element targeting.

### Data Processing & Utilities
- `delete_duplicates()` — Purges duplicate values in $O(N)$ linear time using tracking sets.
- `deleteEntireInstanceOfElement(item)` — Safely purges consecutive occurrences of an element.
- `delete_middle()` / `find_middle()` — Utilizes the Fast & Slow pointer technique.
- `has_cycle()` — Implements Floyd's Cycle-Finding Algorithm to detect pointer loops.
- `print_backward()` — Displays elements from back to front using backward pointers.
- `reverse_list()` — Completely rewires internal node references to reverse direction in a single pass.

## 💻 Python Protocols Implemented
- `__len__` — Integration with Python's native `len()` function.
- `__str__` — Clean, human-readable console string formatting (`5 <--> 10 <--> 20 --> None`).
- `__iter__` — Custom iterator implementation (`DllIterator`) allowing standard Python loops (`for item in dll:`).

## 📝 Learning Note
This repository was engineered from the ground up by focusing entirely on **visual pointer architecture diagrams** rather than memory syntax. Every single boundary manipulation method safely shields pointer overwrites against edge cases (empty lists, single-node states, and multi-node bounds)
