class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        # TODO: Add item to the top of the stack
        self.stack.append(item)

    def pop(self):
        # TODO: Remove and return the top item of the stack if not empty
        if self.is_empty():
            return "Array is empty!"
        last=self.stack.pop()
        return last
        # return self.stack(len(self.stack)-1)

    def peek(self):
        # TODO: Return the top item without removing it
        if self.is_empty():
            return "Array is empty!"
        return self.stack[-1]
    def is_empty(self):
        # TODO: Return True if the stack is empty, otherwise False
        if len(self.stack)==0:
            return True
        return False

    def display(self):
        # TODO: Print all elements from top to bottom
        print("Elements in array are:")
        for i in self.stack:
            print(i)

    def size(self):
        # TODO: Return the number of items in the stack
        return len(self.stack)

    def clear(self):
        # TODO: Remove all elements from the stack
        self.stack.clear()

    def search(self, value):
        # TODO: Return the 1-based position of value from top if found
        if self.is_empty():
            return "Array is empty!"
        for i in range(len(self.stack)):
            if self.stack[i]==value:
                return i+1
        return "Value does not exist!"
    
    def reverse(self):
        # TODO: Reverse the order of the stack (bottom becomes top and vice versa).
        n=len(self.stack)
        for i in range(n//2):
            temp=self.stack[i]
            self.stack[i]=self.stack[n-i-1]
            self.stack[n-i-1]=temp
        #self.stack.reverse()

    def copy(self):
        # TODO: Return a new copy of the stack
        new_array=[]
        for i in self.stack:
            new_array.append(i)
        return new_array

    def multi_pop(self, n):
        # TODO: Pop n elements from the stack if possible
        if n>len(self.stack):
            return "out of bound!"
        for _ in range(n):
            self.stack.pop()

    def peek_n(self, n):
        # TODO: Return the nth item from the top without removing it
        if n>len(self.stack) or n<=0:
            return "out of bound!"
        return self.stack[n-1]