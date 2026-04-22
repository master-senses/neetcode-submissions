class LinkedNode:
    def __init__(self, val: int, next_node: Optional['LinkedNode'] = None):
        self.value = val
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head: Optional[LinkedNode] = None
        self.tail: Optional[LinkedNode] = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        current = self.head
        for i in range(index):
            if current.next_node is None:
                return -1
            current = current.next_node
        return current.value

    def insertHead(self, val: int) -> None:
        new_node = LinkedNode(val, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = LinkedNode(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return True
        current = self.head
        for i in range(index - 1):
            if current.next_node is None:
                return False
            current = current.next_node
        if current.next_node is None:
            return False
        current.next_node = current.next_node.next_node
        if current.next_node is None:
            self.tail = current
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next_node
        return values

        
