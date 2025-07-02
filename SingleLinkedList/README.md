# 🪢 SingleLinkedList in Python

This project contains:
- `SingleLinkedList.py`: The implementation of a singly linked list.
- `test_cases.py`: A test script covering key operations.

## 📦 Features
- Insert at beginning, end, or any index
- Delete from beginning, end, or any index
- Search for a value
- Get or set value by index
- Reverse the list
- Merge two linked lists
- Find the n-th node from the end
- Clear the list, get length, check if empty
- Convert to/from Python list
- Sort the list
- Get the middle node

## 🧪 How to Run Tests

```bash
python test_cases.py
```

The script will print and validate operations using assert statements.

## ✏️ Example Usage

```python
from SingleLinkedList import SingleLinkedList

ll = SingleLinkedList()
ll.insert_at_end(10)
ll.insert_at_beginning(5)
ll.insert_at_index(1, 7)
print(ll.to_list())   # [5, 7, 10]
```

✨ *Happy coding!*
