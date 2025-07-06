class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # New tail pointer
        self.size = 0   # <-- Tracks number of elements in the list

    def insert(self, data):
        """Insert a node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node  # Update tail when first node is added
        else:
            self.tail.next = new_node
            self.tail = new_node  # Update tail to the new node
        self.size += 1  # Update size

    def remove(self, key):
        """Remove the first node with the given data"""
        current = self.head
        prev = None

        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                # If removing the tail node, update the tail
                if current == self.tail:
                    self.tail = prev

                current = None
                self.size -= 1  # Update size
                return
            prev = current
            current = current.next

        print(f"Node with data {key} not found.")

    def find(self, key):
        """Check if a node with the given data exists"""
        current = self.head
        while current:
            if current.data == key:
                print(f"Node with data {key} found.")
                return True
            current = current.next
        print(f"Node with data {key} not found.")
        return False

    def traverse(self):
        """Traverse and print the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insertAtFront(self, data):
        """Insert a node at the beginning of the list"""
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insertAtEnd(self, data):
        """Insert a node at the end of the list (same as insert using tail)"""
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def removeFromFront(self):
        """Remove the node at the beginning of the list"""
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def removeFromBack(self):
        """Remove the node at the end of the list"""
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.size -= 1

    def getElementAt(self, index):
        """Return the data at the specified index (0-based)."""
        if index < 0 or index >= self.size:
            return "Index out of bond"
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def insertSorted(self, data):
        """Insert a node while maintaining ascending sorted order."""
        # Case 1: List is empty
        # Case 2: Insert at the front
        if self.head == self.tail == None:
            self.insertAtFront(data)
        else:
            self.insertAtFront(data)
            self.selection_sort()

    def selection_sort(self):
        """Sort the list in ascending order using selection sort"""
        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            temp = current.data
            current.data = min_node.data
            min_node.data = temp
            current = current.next

# Usage Example
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert(10)
    ll.insert(20)
    ll.insert(30)

    ll.traverse()  # Output: 10 -> 20 -> 30 -> None

    ll.find(20)    # Output: Node with data 20 found.
    ll.find(40)    # Output: Node with data 40 not found.

    ll.remove(30)  # Removing the tail
    ll.traverse()  # Output: 10 -> 20 -> None

    ll.remove(10)  # Removing the head
    ll.traverse()  # Output: 20 -> None

    ll.remove(20)  # Removing the last remaining node
    ll.traverse()  # Output: None

    # Now list is empty; insert again
    ll.insert(50)
    ll.traverse()  # Output: 50 -> None
