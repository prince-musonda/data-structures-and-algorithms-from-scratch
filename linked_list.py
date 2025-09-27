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
    
    def prepend(self,value):
        # case 1: list is empty
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        # case 2: list is not empty
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def pop(self):
        #if no item is available:
        if self.head is None:
            return None
        # if only one item  availble in the list
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
            self.tail = prev
            self.length -= 1
            return temp
        
    def pop_first(self):
        # case1: list is empty
        if self.head is None:
            return None
        # case2
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
    
    def get(self,index):
        #case: if the the list is empty or requested index not in list, or used a negative index:
        if self.head is None or index >= self.length or index < 0:
            return None
        #case: if index is of the last item in the list
        elif (index+1) == self.length:
            return self.tail
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp


    def set_value(self,index,value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        else:
            return False



    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


