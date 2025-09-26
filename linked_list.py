# # class Node:
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# # class LinkedList:
class LinkedList:
    def __init__(self,value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        # check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def preappend(self,value):
        new_node = Node(value)
        first_node = self.head
        self.head = new_node
        self.head.next = first_node
        self.length += 1

    def pop(self):
        #if no item is available:
        if self.head is None:
            return None
        # if only one item is availble in the list
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node
        # else if 2 or more items exist, find the second last item, and set next = None
        else:
            temp = self.head
            prev = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None
            self.tail = next
            self.length -= 1
            return temp


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = LinkedList(3)
my_list.preappend(2)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.preappend(1)
my_list.pop()
my_list.pop()
my_list.pop()


my_list.print_list()

 

                                                                                                                 