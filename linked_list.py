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
        return True
    
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


    def insert(self,index,value):
        # case: index less than zero or greater than length
        if index < 0 or index > self.length:
            return False
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        #case index is first node
        elif index == 0:
            self.length -=1
            return self.pop_first()
        #case: index is of the last item
        elif index == (self.length-1):
            return self.pop()
        #case: index is of any item in the middle
        else:
            prev_node= self.get(index-1)
            temp = prev_node.next
            after_node = prev_node.next.next
            prev_node.next = after_node
            temp.next = None
            self.length -= 1
            return temp
            
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        prev = None
        after = temp.next
        while temp is not None:
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = LinkedList(12)
my_list.append(13)
my_list.append(14)
my_list.append(15)
my_list.reverse()
my_list.print_list()

nodes = {my_list.head : 0}
nodes[my_list.head.next] = 1

print(nodes[my_list.head.next])