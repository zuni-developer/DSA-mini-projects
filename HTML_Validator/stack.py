class Stack:
    """A simple implementation of a Stack (LIFO) similar to java.util.Stack."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Pushes an item onto the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Removes and returns the item at the top. Returns None if empty."""
        return self._items.pop() if not self.is_empty() else None

    def peek(self):
        """Returns the top item without removing it. Returns None if empty."""
        return self._items[-1] if not self.is_empty() else None

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Returns the number of items in the stack."""
        return len(self._items)

    def clear(self):
        """Removes all elements from the stack."""
        self._items.clear()

    def contains(self, item):
        """Returns True if the item is in the stack."""
        return item in self._items

    def to_list(self):
        """Returns a shallow copy of the stack as a list."""
        return self._items.copy()


    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._items)

    def __iter__(self):
        """Allow iteration from bottom to top."""
        return iter(self._items)

    def __eq__(self, other):
        """Define equality for test comparisons."""
        if not isinstance(other, Stack):
            return False
        return self._items == other._items

    def __str__(self):
        return f"Stack({self._items})"
