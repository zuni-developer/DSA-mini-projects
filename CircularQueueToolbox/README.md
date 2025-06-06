# CircularQueueToolbox

**CircularQueueToolbox** is a custom Python class that implements a circular queue data structure with fixed capacity. It supports essential queue operations such as enqueue, dequeue, peek, and capacity checks, making it a useful component in scenarios where bounded memory usage and efficient data cycling are required.

---

## 📦 Features

- Enqueue and dequeue operations with circular indexing
- Front and rear pointer management
- Size tracking and capacity checks
- Clear/reset functionality
- Safe handling of underflow and overflow conditions

---

## 📂 File Structure

```
CircularQueueToolbox/
├── CircularQueueToolbox.py     # Core circular queue class
├── test_cases.py               # Test cases for validation
├── main.py                     # CLI-based interactive runner
└── README.md                   # Project documentation
```

---

## 🔧 Class Overview

### `CircularQueueToolbox(capacity: int)`

#### Methods:

| Method         | Description |
|----------------|-------------|
| `enqueue(item)` | Adds an item to the rear of the queue. Returns an error message if full. |
| `dequeue()`     | Removes and returns the front item. Returns `None` if empty. |
| `peek()`        | Returns the front item without removing it. |
| `is_empty()`    | Returns `True` if the queue is empty. |
| `is_full()`     | Returns `True` if the queue is full. |
| `size()`        | Returns the current number of items in the queue. |
| `clear()`       | Resets the queue, clearing all elements. |

---

## 🧪 Test Cases

The `test_circular_queue.py` file contains unit-style test cases to validate queue functionality.

### ✅ Sample Test

```python
from CircularQueueToolbox import CircularQueueToolbox

def test_basic_operations():
    q = CircularQueueToolbox(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.is_full() == True
    assert q.dequeue() == 1
    q.enqueue(4)
    assert q.peek() == 2
    assert q.size() == 3
```

Run test cases:

```bash
python test_cases.py
```

---

## 🚀 How to Use (CLI)

The `main.py` file provides a simple command-line interface for experimenting with the circular queue.

### Example Interaction:

```bash
python main.py
```

```
Circular Queue Menu:
1. Enqueue
2. Dequeue
3. Peek
4. Size
5. Clear
6. Exit
Enter your choice:
```

---

## 🧠 Use Cases

- Task scheduling in circular buffers
- Fixed-size data stream processing
- Memory-constrained embedded systems
- Round-robin algorithms

---
