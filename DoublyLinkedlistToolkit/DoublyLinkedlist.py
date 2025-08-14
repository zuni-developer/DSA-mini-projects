class Node:
    def __init__(self, data):
        self.data=data  # Stores the value of the node
        self.prev=None  # Points to the previous node
        self.next=None  # Points to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head=None  # Stores the first node of the list
        self.size=0  # Stores the total number of elements of the list

    def insert_at_beginning(self, data):
        # Inserts a new node at the start of the list
        if self.head is None:
            self.head=Node(data)
            self.size+=1
            return
        current=self.head
        new=Node(data)
        self.head=new
        new.next=current
        current.prev=new
        self.size+=1
            
    def insert_at_end(self, data):
        # Inserts a new node at the end of the list
        if self.head is None:
            self.head=Node(data)
            self.size+=1
            return
        current=self.head
        new=Node(data)
        while current.next is not None:
            current=current.next
        current.next=new
        new.prev=current
        self.size+=1

    def insert_after_node(self, target_data, data):
        # Inserts a new node after a specific node with given data
        current=self.head
        while current:
            if current.data==target_data:
                new=Node(data)
                new.next=current.next
                new.prev=current
                if current.next:
                    current.next.prev = new
                current.next=new
                self.size+=1
                return
            current=current.next

    def insert_before_node(self, target_data, data):
        # Inserts a new node before a specific node with given data
        current=self.head
        while current:
            if current.data==target_data:
                new=Node(data)
                new.next=current
                new.prev=current.prev
                if current.prev:
                    current.prev.next=new
                else:
                    self.head=new
                current.prev=new
                self.size+=1
                return
            current=current.next
            
    def delete_at_beginning(self):
        if self.head is None:
            return
        if self.head.next:
            self.head=self.head.next
            self.head.prev=None
        else:
            self.head=None
        self.size-=1

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
        else:
            current=self.head
            while current.next:
                current=current.next
            current.prev.next=None
        self.size-=1

    def delete_node(self, key):
        # Deletes the first node with the given value
        current=self.head
        while current:
            if current.data==key:
                if current.prev:
                    current.prev.next=current.next
                else:
                    self.head=current.next
                if current.next:
                    current.next.prev=current.prev
                self.size-=1
                return
            current=current.next

    def delete_at_position(self, position):
        # Deletes a node at a specific index (0-based)
        if position<0 or position>=self.size:
            return
        if position==0:
            self.delete_at_start()
            return
        current=self.head
        index=0
        while current and index<position:
            current=current.next
            index+=1
        if current:
            if current.prev:
                current.prev.next=current.next
            if current.next:
                current.next.prev=current.prev
            self.size-=1

    def search(self, key):
        # Searches for a node with the given value and returns True if found
        current=self.head
        while current is not None:
            if current.data==key:
                return True
            current=current.next
        return False

    def update_node(self, old_value, new_value):
        # Updates the first node with old_value to have new_value
        current=self.head
        while current is not None:
            if current.data==old_value:
                current.data=new_value
                break
            current=current.next

    def display_forward(self):
        # Displays the list from head to tail
        result=[]
        current=self.head
        while current:
            result.append(current.data)
            current=current.next
        return result

    def display_backward(self):
        # Displays the list from tail to head
        result=[]
        current=self.head
        if not current:
            return result
        while current.next:
            current=current.next
        while current:
            result.append(current.data)
            current=current.prev
        return result

    def get_length(self):
        # Returns the number of nodes in the list
        return self.size

    def is_empty(self):
        # Returns True if the list is empty
        if self.head is None:
            return True
        return False

    def clear(self):
        # Removes all nodes from the list
        self.head=None
        self.size=0

    def reverse(self):
        # Reverses the order of the linked list
        current=self.head
        prev_node=None
        while current:
            prev_node=current.prev
            current.prev=current.next
            current.next=prev_node
            current=current.prev
        if prev_node:
            self.head=prev_node.prev

    def get_first(self):
        # Returns the value of the first node
        if self.head is None:
            return None
        return self.head.data

    def get_last(self):
        # Returns the value of the last node
        current=self.head
        while current.next is not None:
            current=current.next
        return current.data

    def get_at_position(self, position):
        # Returns the value of the node at the given index (0-based)
        if position<0 or position>=self.size:
            return None
        current=self.head
        index=0
        while current and index<position:
            current=current.next
            index+=1
        return current.data if current else None

    def sort_ascending(self):
        # Sorts the list in ascending order
        if self.size<2:
            return
        swapped=True
        while swapped:
            swapped=False
            current=self.head
            while current and current.next:
                if current.data>current.next.data:
                    temp=current.data
                    current.data=current.next.data
                    current.next.data=temp
                    swapped=True
                current=current.next

    def sort_descending(self):
        # Sorts the list in descending order
        if self.size<2:
            return
        swapped=True
        while swapped:
            swapped=False
            current=self.head
            while current and current.next:
                if current.data<current.next.data:
                    temp=current.data
                    current.data=current.next.data
                    current.next.data=temp                    
                    swapped=True
                current=current.next

    def merge_with(self, other_list):
        # Merges the current list with another doubly linked list
        if self.head is None:
            self.head=other_list.head
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=other_list.head
            if other_list.head:
                other_list.head.prev=last
        self.size+=other_list.size

    def remove_duplicates(self):
        # Removes duplicate values from the list
        current=self.head
        while current:
            pointer=current.next
            while pointer:
                if pointer.data==current.data:
                    if pointer.prev:
                        pointer.prev.next=pointer.next
                    if pointer.next:
                        pointer.next.prev=pointer.prev
                    self.size-=1
                pointer=pointer.next
            current=current.next

    def to_list(self):
        # Converts the linked list to a Python list
        arr=[]
        current=self.head
        while current:
            arr.append(current.data)
            current=current.next
        return arr

    def from_list(self, data_list):
        # Creates a linked list from a Python list
        self.clear()
        for value in data_list:
            self.insert_at_end(value)
