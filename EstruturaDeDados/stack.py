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

s = Stack()
s.push(5)
s.push(7)
s.push(11)
print(s.top.data)
print(s.top.next.data)
s.pop()
print(s.top.data)

