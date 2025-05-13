class FixedSizeArray:
    def __init__(self, size):
        self.size=size
        self.length=0
        self.data=[None]*size

    def free_index(self,index):
        if index>=len(self.data):
            print("Invalid index! free indices are: ")
            for i in range(len(self.data)):
                if self.data[i]==None:
                    print(i,end=" ")
                print("\n")
            return True
        return False
        
    def out_of_bond(self,index):
        if self.length>=self.size or index<0 or index>self.length:
            print("Cannot insert: Index out of bond!")
            return True
        return False
        
    def insert(self, index, value):
        # Insert value at specified index
        if self.is_full():
            self.data=self.resized_array()
        if self.free_index(index) or self.out_of_bond(index):
            return
        j=self.length-1
        while j>=index:
            self.data[j+1]=self.data[j]
            j-=1
        self.data[index]=value
        self.length+=1

    def delete(self, index):
        # Delete value at specified index
        if index<0 or index>=self.length:
            print("Invalid index!")
            return
        value=self.data[index]
        j=index
        while j<self.length-1:
            self.data[j]=self.data[j+1]
            j+=1
        self.data[self.length-1]=None
        self.length-=1

    def update(self, index, value):
        # Update value at specified index
        if index<self.length and index>=0:
            self.data[index]=value
        else:
            print("Index out of bounds!")

    def get(self, index):
        # Return value at specified index
        if index<self.length and index>=0:
            return self.data[index]
        else:
            print("Index out of bounds!")

    def display(self):
        # Return the list of current elements
        if self.is_empty():
            print("Array is empty!")
            return
        print("The elements in the array are:")
        for i in range(self.length):
            print(self.data[i])

    def print(self):
        # Print array in [a, b, c] format
        print("[", end="")
        for i in range(self.length):
            print(self.data[i], end="")
            if i!=self.length-1:
                print(", ", end="")
        print("]")

    def search(self, value):
        # Return index of first occurrence of value or -1 if not found
        flag=False
        for i in range(self.length):
            if self.data[i]==value:
                print("The Element was found at:", i)
                flag=True
                break
        if not flag:
            print("The element was not found!")

    def is_full(self):
        # Return True if array is full
        if self.length==self.size:
            return True
        return False

    def is_empty(self):
        # Return True if array is empty
        if self.length==0:
            return True
        return False

    def clear(self):
        # Clear the array (reset all elements)
        for i in range(self.length):
            self.data[i] = None
        self.length = 0
        
    def resized_array(self):
        self.size*=2
        new_arr=[None]*(self.size)
        for i in range(self.length):
            new_arr[i]=self.data[i]
        return new_arr
    
    def bubble_sort(self):
        min = self.data[0]
        for i in range(self.length-1):
            for j in range(self.length-i-1):
                if(self.data[j]>self.data[j+1]):
                    min = self.data[j+1]
                    self.data[j+1] = self.data[j]
                    self.data[j] = min
    
    def binary_search(self,value):
        low=0
        high=self.length-1
        while low<=high:
            mid=(low+high)//2
            if self.data[mid]==value:
                return mid
            elif self.data[mid]<value:
                low=mid+1
            else:
                high=mid-1
        return -1