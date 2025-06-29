class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        self.append(data)

    def insert_at_index(self, index, data):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        self.size -= 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.size -= 1

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def length(self):
        return self.size

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_middle(self):
        mid = self.size // 2
        current = self.head
        for _ in range(mid):
            current = current.next
        return current

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index, value):
        if index < 0 or index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def remove_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, lst):
        for item in lst:
            self.append(item)

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_current = sorted_head
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_head

    def merge(self, other_list):
        if self.head is None:
            self.head = other_list.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other_list.head
        self.size += other_list.size

    def find_nth_from_end(self, n):
        index = self.size - n
        if index < 0:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data