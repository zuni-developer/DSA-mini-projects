# 📦 StackToolbox - Custom Stack Operations in Python

## 📌 Project Overview

**StackToolbox** is a Python-based stack implementation that goes beyond the basics. It provides a range of stack operations, ideal for students and developers looking to strengthen their understanding of **Data Structures and Algorithms (DSA)** through a hands-on approach.

All operations are built from scratch — no use of built-in stack libraries — making this an educational and practical resource for mastering core concepts.

---

## 🧠 DSA Concepts Covered

* Stack basics: Push, Pop, Peek
* Stack inspection: Size, Is Empty
* Advanced operations: Reverse, Copy, Multi-Pop, Search, Peek-N
* Defensive programming and edge case handling

---

## 🚀 Features

### ✅ `push(item)`

Adds an element to the top of the stack.

### ✅ `pop()`

Removes and returns the top element. If the stack is empty, returns a warning message.

### ✅ `peek()`

Returns the top element without removing it.

### ✅ `display()`

Prints all elements from bottom to top.

### ✅ `size()`

Returns the number of elements in the stack.

### ✅ `is_empty()`

Checks if the stack is empty. Returns `True` or `False`.

### ✅ `clear()`

Removes all elements from the stack.

### ✅ `search(value)`

Returns the **1-based position from the top** of a specified value. Returns a message if the value is not found.

### ✅ `reverse()`

Reverses the stack in-place.

### ✅ `copy()`

Returns a **new list** that is a copy of the current stack.

### ✅ `multi_pop(n)`

Pops `n` elements from the top. Returns a warning if `n` is out of bounds.

### ✅ `peek_n(n)`

Returns the `n`th element from the top without removing it. Handles invalid positions.

---

## 🧪 Sample Usage

```python
from stack_operations import Stack

stack = Stack()
stack.push(10)
stack.push(20)
print("Top:", stack.peek())  # Output: 20
stack.pop()
print("Is empty?", stack.is_empty())  # Output: False
```

---

## 📁 Files

* `stack_operations.py` – Contains the `Stack` class and all methods.
* `main.py` – CLI-based interface for users to interact with stack operations.

---

## 🧰 Ideal For

* DSA beginners practicing stacks.
* Students preparing for coding interviews.
* Developers creating lightweight utility modules.

---

## 📜 License

This project is intended for educational use. Feel free to use, modify, and learn from it!
