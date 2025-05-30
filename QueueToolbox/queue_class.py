class Queue:
    def __init__(self):
        self._items=[]  # Internal list to store queue elements

    # Add an item to the end of the queue
    def enqueue(self, item):
        self._items.append(item)

    # Remove and return the front item. Return None if empty
    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    # Return the front item without removing it. Return None if empty
    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    # Return True if the queue is empty, else False
    def is_empty(self):
        if len(self._items)==0:
            return True
        return False

    # Return the number of items in the queue
    def size(self):
        return len(self._items)

    # Remove all items from the queue
    def clear(self):
        self._items.clear()

    # Return True if the item is in the queue
    def contains(self, item):
        for i in self._items:
            if i==item:
                return True
        return False