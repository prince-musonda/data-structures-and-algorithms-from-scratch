class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
       


class Stack:
    def  __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        # case: stack is empty
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return True
    
    def pop(self):
        # case: stack is empty
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -= 1
            return temp
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    
my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)
my_stack.push(0)

print("before poping")

my_stack.print_stack()

my_stack.pop()
my_stack.pop()
print("after pop")
my_stack.print_stack()