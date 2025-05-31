# QueueToolbox - Custom Queue Implementation in Python

## 📌 Project Overview

**QueueToolbox** is a lightweight and educational Python class that provides custom queue operations without using Python's built-in data structure methods like `collections.deque`. This project is built to strengthen understanding of **Data Structures and Algorithms (DSA)** by manually implementing core queue functionalities.

Whether you're a beginner learning queues or brushing up on basic algorithmic thinking, this project is a great hands-on tool.

---

## 🧠 DSA Concepts Covered

- FIFO (First-In-First-Out) logic
- Element access and removal
- Search and containment checks
- Size tracking and memory clearing
- Defensive programming for empty queue scenarios

---

## 🚀 Features

### ✅ `enqueue(item)`
- Adds an item to the end of the queue.
- Time complexity: O(1)

### ✅ `dequeue()`
- Removes and returns the item at the front of the queue.
- Returns `None` if the queue is empty.
- Time complexity: O(n) due to list shifting.

### ✅ `peek()`
- Returns the front item without removing it.
- Returns `None` if the queue is empty.

### ✅ `is_empty()`
- Returns `True` if the queue has no items.
- Returns `False` otherwise.

### ✅ `size()`
- Returns the total number of items in the queue.

### ✅ `clear()`
- Empties the entire queue.

### ✅ `contains(item)`
- Returns `True` if the item exists in the queue.
- Linear search used (O(n)).

---

## 🧪 Sample Usage

```python
from queue_toolbox import Queue

q = Queue()

q.enqueue('apple')
q.enqueue('banana')
q.enqueue('cherry')

print(q.dequeue())       # Output: apple
print(q.peek())          # Output: banana
print(q.contains('banana'))  # Output: True
print(q.is_empty())      # Output: False
print(q.size())          # Output: 2
q.clear()
print(q.size())          # Output: 0
