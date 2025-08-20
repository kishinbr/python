from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head = new_node
           return 
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return
    
    def length(self):
        current_node = self.head
        total = 0

        while current_node:
            total +=1
            current_node = current_node.next
        return total

    def to_list(self):
        node_data = []       
        current_node = self.head
        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def display(self):
        contets = self.head
        if contets is None:
            print("List has no element")
            return
        while contets:
            print(contets.data)
            contets = contets.next
        print("------")

    def revert_linkedlist(self):
        previous_node = None
        current_node = self.head
        
        while current_node != None:
            next = current_node.next

            current_node.next = previous_node
            previous_node = current_node
            current_node = next

        self.head = previous_node

    def get(self, index):
        if index < 0:
            raise IndexError("List index out of range")

        current_idx = 0
        current_node = self.head
        while current_node is not None:
            if current_idx == index:
                return current_node.data
            current_node = current_node.next
            current_idx += 1

        raise IndexError("List index out of range")


    def search_item(self,item):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == item:
                return print(f"{i}")
            pointer = pointer.next
            i+=1
        print(f"{item} is not in list")


    def remove_at_start(self):
        if self.head is None:
            raise IndexError("remove from empty list")  

        removed_data = self.head.data  
        self.head = self.head.next    
        return print(f"{removed_data} has remove from list")


    def remove_at_end(self):
        if self.head is None:
            raise IndexError("remove from empty list") 
        
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data

        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        
        removed_data = current_node.next.data  
        current_node.next = None 
        return removed_data


    
    def insert_at_start(self,value):
        if self.head:
            current_node = self.head
            self.head = Node(value)
            self.head.next = current_node
        else:
            self.head = Node(value)



    def insert_at_end(self,value):
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)
        else:
            self.head = Node(value)

    def remove_element_by_value(self, value):

        if self.head is None:
            raise ValueError("The list is empty")

        current_node = self.head
        index = 0

       
        if current_node.data == value:
            self.head = current_node.next
            return index

        
        while current_node.next:
            index += 1
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return index
            current_node = current_node.next

        raise ValueError(f"{value} was not found in the list")

    
    def insert_at_index(self, index, value):
        if index < 0:
            raise IndexError("list index out of range")
        
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        i = 0
        while i < index - 1:
            if current_node is None:
                raise IndexError("list index out of range")
            current_node = current_node.next
            i += 1
        
        if current_node is None:
            raise IndexError("list index out of range")
        
        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node

    


my_list = LinkedList()

my_list.display()

my_list.append(3)
my_list.append(7)
my_list.append(2)
my_list.append(1)

my_list.display()

print(f"The total number of elements are: {str(my_list.length())}")
print(my_list.to_list())

my_list.revert_linkedlist()
my_list.display()


my_list.remove_at_start()
print("---")
my_list.display()
print("---")

my_list.remove_at_end()
my_list.display()
