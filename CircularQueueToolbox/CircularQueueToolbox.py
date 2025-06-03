class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    # Add item to the rear. Handle overflow.
    def enqueue(self, item):
        if self.is_full():
            return "Queue is full!"
        if self.is_empty():
            self.front=0
            self.rear=0
        else:
            self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=item
    
    # Remove and return the front item. Handle underflow.    
    def dequeue(self):
        if self.is_empty():
            return None
        
        item=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.capacity
        return item
    
    # Return front item without removing it.    
    def peek(self):
        return self.queue[self.front]
    
    # Check if queue is empty.
    def is_empty(self):
        if self.rear==-1 and self.front==-1:
            return True
        return False
    
    # Check if queue is full.
    def is_full(self):
        if self.front==(self.rear+1)%self.capacity:
            return True
        return False
    
    # Return the number of items in the queue.
    def size(self):
        if self.is_empty():
            return 0
        if self.rear>=self.front:
            return self.rear-self.front+1
        return self.capacity-(self.front-self.rear-1)
    
    # Reset the queue.
    def clear(self):
        self.queue=[None]*self.capacity
        self.front=-1
        self.rear=-1
        self.count=0