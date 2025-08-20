from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
            self.size += 1
        else:
            self.head = Node(elem)
            self.size += 1


    #a = lista[6]
    #a = lista.get(6)
    def __getitem__(self,index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    
    def __setitem__(self,index,elem):
        #lista[5] = 9
        #lista.set(5,9)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
    
    def index(self, elem):
        pointer =self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i +=1
        raise ValueError(f"{elem} is not in list")
    


    def show(self):
        l = list()
        pointer = self.head
        if self.head:
            for i in range(self.size):
                l.append(pointer.data)
                pointer = pointer.next
            return l
        else:
            raise IndexError("list has no elements")


    def __len__(self):
        return self.size
    
if __name__ == "__main__":
    
    lista = LinkedList()
    lista.append(10)
    lista.append(11)
    lista.append(12)

    print(lista.show())

    print(lista[0])
    lista[0] = 50

    print(lista.show())

    print(lista.index(12))
    print(lista.index(1))