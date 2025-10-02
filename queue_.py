class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    

class Queue():
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self, value):
        new_node = Node(value)
        # case: check if queue is empty
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        # case: queue is empty
        if self.first is None:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            # reassign self.last if necessary
            if self.first is None:
                self.last = None
            # reduce length
            self.length -= 1
            return temp
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_queue = Queue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.print_queue()
print(f"--- removing from the queue---------")
print(f"removing: {my_queue.dequeue().value}")
print(f"removing: {my_queue.dequeue().value}")
print(f"removing: {my_queue.dequeue().value}")
print(f"removing: {my_queue.dequeue().value}")
my_queue.print_queue()
print(my_queue.last)
