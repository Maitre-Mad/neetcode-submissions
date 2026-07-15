class DynamicArray:
    ##SETUP INIT
    def __init__(self, capacity: int):
        ##we set up the capacity|allocated memory
        self.capacity=capacity
        ##elemens that are actually being used rightnow
        self.size=0
        ##allocates a fixed size list in memory filled with zeros as starting storage
        self.arr=[0]*self.capacity

    ##looks at index i in our storage array and return the value that sti there
    def get(self, i: int) -> int:
        return self.arr[i]

    ##goes straight to index i and overwrites it with athe new number n
    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    ##This add a new element n to the very end of the array
    def pushback(self, n: int) -> None:
        if self.size ==self.capacity:#check if the arrays is completely full, if it is we resize
            self.resize()
        self.arr[self.size]=n##arrays are 0 indexed, the curren size always amtches the index of the empty slot
        self.size+=1##it increments by 1 because we added an element

    #Remove Data
    def popback(self) -> int:
        #we decrease the size of the array by 1 
        self.size-=1
        return self.arr[self.size]

    #when the array is full, we just stretch the existing memory block 
    def resize(self) -> None:
        #double the capacity
        self.capacity*=2
        #we create a brand new,empty array that is twice as big
        new_arr=[0]*self.capacity
        #loop copies every element from the old, and put it into the new array 
        for i in range(self.size):
            new_arr[i]=self.arr[i]
        #we update the address 
        self.arr=new_arr

    #this get us the info for the size of the array
    def getSize(self) -> int:
        return self.size
    
    #this check for the actual capcity left 
    def getCapacity(self) -> int:
        return self.capacity
    
