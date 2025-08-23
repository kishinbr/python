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

    def pop(self):
        if self.head is None:
            raise ValueError("list is empty")
        
        data = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -=1

        return data
    def remove(self,elem):
        if self.head is None:
            raise ValueError("list is empty")
        
        current = self.head
        while current:
            if current.data == elem:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -=1
                return current.data
            current = current.next

        raise ValueError(f"{elem} is not in list")
            
            
    def __setitem__(self,index,value):
        if index < 0 or index >= self.size or self.head is None:
            raise IndexError("list index out of range")
        
        if index >= self.size//2:
            current = self.tail
            for _ in range(self.size - 1,index,-1):
                current = current.prev
        else:
            current = self.head
            for _ in range(index):
                current = current.next
        current.data = value

        
    
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
