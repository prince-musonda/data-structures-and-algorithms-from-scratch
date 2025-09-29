class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        # case: list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        #case list is not empty
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # case: list is empty
        if self.head is None:
            return None
        # case: list contains 1 item only
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            before = temp.prev
            before.next = None
            temp.prev = None
            self.tail = before
        self.length -= 1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        # case: list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length -= 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = DoublyLinkedList(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.prepend(2)
my_list.print_list()


