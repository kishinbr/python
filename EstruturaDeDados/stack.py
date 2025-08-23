from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,data):
        if self.top is None:
            self.top = Node(data)
        else:
            aux = self.top
            self.top = Node(data)
            self.top.next = aux

        self.size +=1

    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def peek(self):
        if self.top is Node:
            raise ValueError("stack is empty")
        return self.top.data



    def display(self):
        if self.top is None:
            raise ValueError("stack is empty")
        
        l = list()
        current_node = self.top
        while current_node:
            l.append(current_node.data)
            current_node = current_node.next
        return l

    def __len__(self):
        return self.size
    
s = Stack()
s.push(5)
s.push(7)
s.push(11)
print(s.display())
print(s.top.data)
print(s.top.next.data)
s.pop()
print(s.top.data)



