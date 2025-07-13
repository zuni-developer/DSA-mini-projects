# 📝 SpecialListToolBox

**SpecialListToolBox** is a custom Python list-like class that supports **undo** and **redo** operations on insertions and deletions.
It preserves insertion order, handles repeated undos/redos, and ignores duplicate insertions gracefully.

---

## 🚀 Features

✅ `insert(value)`
• Inserts a new value (only if it doesn't already exist).
• Adds the action to the undo history.

✅ `delete(value)`
• Deletes the value if it exists.
• Adds the action to the undo history.

✅ `undo()`
• Undoes the last insert or delete operation.
• Safely handles edge cases like trying to undo non-existing deletes.

✅ `redo()`
• Redoes the last undone action.
• Clears redo history on new insert/delete.

✅ `display()`
• Prints the current state of the list.

✅ Supports clear separation of **undo history** and **redo history**.

---

## 🧪 Test Cases

The project includes a rich set of structured test cases covering:

* Normal insert/delete/undo/redo flows
* Multiple undos/redos
* Handling of non-existing deletes
* Duplicate insertions
* Edge scenarios

Just run the script directly to see all tests in action.

---

## 🛠️ Usage Example

```python
from special_list import SpecialList 

lst = SpecialList()
lst.insert(10)
lst.insert(20)
lst.delete(10)
lst.undo()   # Undo delete(10)
lst.redo()   # Redo delete(10)
lst.display()  # Should reflect current state
```