class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,elem):
        new_node = Node(elem)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def __getitem__(self,index):
    
        if index < 0 or index >= self.size or self.head is None:
            raise IndexError("list index out of range")
        
        if index == 0 :
            return self.head.data
            
        if index >= self.size//2:
            current = self.tail
            for _ in range(self.size-1,index,-1):
                current = current.prev
            
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            
        return current.data
                


    
    
    
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data   
            current = current.next

    def __str__(self):
        elems = []
        current = self.head
        while current:
            elems.append(str(current.data))
            current = current.next
        return " <-> ".join(elems)   
