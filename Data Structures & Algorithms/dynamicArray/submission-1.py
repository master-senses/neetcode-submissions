class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None]*capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def resize(self) -> None:
        new_array = [None]*self.getCapacity()*2
        for i in range(self.getCapacity()):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = self.getCapacity()*2
    
    def getCapacity(self) -> int:
        return self.capacity


    def getSize(self) -> int:
        # size = 0
        # while ((size < self.getCapacity()) and (self.get(size) is not None)):
        #     size += 1
        return self.size

    def pushback(self, n: int) -> None:
        if (self.getSize() >= self.getCapacity()):
            self.resize()
            self.set(self.getSize(), n)
            self.size += 1
            return
        self.set(self.getSize(), n)
        self.size += 1

    def popback(self) -> int:
        element = self.get((self.getSize() - 1))
        # self.array.pop((self.getSize() - 1))
        self.size -= 1
        return element
