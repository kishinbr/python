from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,elem):
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(elem)
        else:
            self.head = Node(elem)
        self.size +=1
            

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def __setitem__(self,index,elem):
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")
        
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = elem 

    def index(self,elem):
        current_node = self.head
        i = 0
        while current_node:
            if current_node.data == elem:
                return i
            i+=1
            current_node = current_node.next
        raise ValueError(f"{elem} is not in list")
    
    def pop(self,index=None):
        if self.head is None:
            raise IndexError("pop from empty list")
        if index is None:
            index = self.size - 1
        if index < 0 or index > self.size:
            raise IndexError("list index out of range")
        
        if index == 0:
            value = self.head.data
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            value = current_node.next.data
            current_node.next = current_node.next.next

        self.size -=1
        return value
    
    def remove(self,elem):
        current_node = self.head
        previus_node = None
        while current_node:
            if current_node.data == elem:
                if previus_node:
                    previus_node.next =current_node.next
                else:
                    self.head = current_node.next
                self.size -=1
                return
            previus_node = current_node
            current_node = current_node.next

        raise ValueError(f"{elem} is not in list")


        

    def __contains__(self,elem):
        current_node = self.head
        while current_node:
            if current_node.data == elem:
                return True
            current_node = current_node.next
        return False
    
    def __delete__(self,index):
        if index <0 or index >= self.size:
            raise IndexError("list index out of range")
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.size -= 1

    def __len__(self):
        if self.head is None:
            return 0
        current_node = self.head
        i =0
        while current_node:
            current_node = current_node.next
            i+=1
        return i
    
    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(elements)
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next


l = LinkedList()
l.append(5)
l.append(7)
l.append(8)
ll = list(l)
print(l)
print(ll)