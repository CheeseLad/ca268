class Queue:
    """
    Python implementation the queue
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def reverse(self):
        tmp = self.dequeue

class Stack:
    """
    Python implementation the stack
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Q3 

input_str = "EAS*Y*QUE***ST***IO*N***"
empty_stack = Stack()
for char in input_str:
    if char != "*":
        empty_stack.push(char)
    else:
        print(empty_stack.pop())

# Q4
input_str = "EAS*Y*QUE***ST***IO*N***"
empty_q = Queue()
for char in input_str:
    if char != "*":
        empty_q.enqueue(char)
    else:
        print(empty_q.dequeue())
