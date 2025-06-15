class MyQueue:
    """A simple FIFO queue implementation, similar to Java's Queue interface."""

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue. Returns None if empty."""
        return self._items.pop(0) if not self.is_empty() else None

    def front(self):
        """Peek at the front item without removing it. Returns None if empty."""
        return self._items[0] if not self.is_empty() else None

    def is_empty(self):
        """Check whether the queue is empty."""
        return len(self._items) == 0

    def __len__(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def clear(self):
        """Remove all elements from the queue."""
        self._items.clear()

    def contains(self, item):
        """Check whether the queue contains a specific item."""
        return item in self._items

    def to_list(self):
        """Return a shallow copy of the queue as a list."""
        return self._items.copy()

    def __str__(self):
        return f"MyQueue({self._items})"


    def __iter__(self):
        """Allow iteration from front to back of the queue."""
        return iter(self._items)

    def __eq__(self, other):
        """Define equality to compare two MyQueue instances."""
        if not isinstance(other, MyQueue):
            return False
        return self._items == other._items
