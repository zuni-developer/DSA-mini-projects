# ListAlgoTools – Custom List Algorithms in Python

## 📌 Project Overview

**ListAlgoTools** is a Python utility class implementing three core list-based algorithms *without relying on built-in functions* like `sort()` or `in` for subsequences. It’s perfect for practicing **Data Structures and Algorithms (DSA)** concepts, using **lists as the primary structure**.

All operations are built from scratch with careful handling of edge cases (`None`, empty lists, invalid inputs), making it a solid educational and foundational coding exercise.

---

## 🧠 DSA Concepts Covered

- Sorted insertion using shifting logic
- Manual sorting (Bubble Sort-like approach)
- Consecutive subsequence detection
- Removal of `N` largest unique values
- Edge case handling and input validation

---

## 🚀 Features

### ✅ `insert_sorted(lst, value)`
- Inserts a value into its correct position in an **already sorted list** (ascending order).
- Uses manual shifting logic to maintain order.
- Does nothing if the list is `None`.

### ✅ `remove_maximum_values(lst, N)`
- Removes the top `N` **largest unique** values from the list.
- Works for both strings and numbers.
- Skips safely if `lst` is `None` or `N <= 0`.

### ✅ `contains_subsequence(one, two)`
- Returns `True` if `two` is found as a **consecutive subsequence** in `one`.
- Implemented with nested loops for manual checking.
- Returns `False` for `None` or empty lists.

---

## 🧪 Test Cases

Each method is thoroughly tested with:
- Valid and invalid inputs
- Boundary conditions (empty lists, over-removal, `None`)
- Subsequence edge scenarios

### To run the test suite:

```bash
python your_file_name.py