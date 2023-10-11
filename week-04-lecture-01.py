# Doing recursion in labs

# He is solving second last question on lab sheet

# Q6

n = 100
m = 0

def recursion(n, m=0):
  if m * (m + 1) < n:
    return recursion(n, m + 1)
  else:
    return m * (m + 1) == n
  
print(recursion(132))

# Time complexity of this solution is _____

# Stack

class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self, item):
    self.items.pop()

  def is_empty(self):
    return len(self.items) == 0
  
  def __len__(self):
    return len(self.items)
  
  def top(self):
    return self.items[-1]
  
# Queue

class Queue:
  def __init__(self):
    self.items = []
  
  def is_empty(self):
    return len(self.items) == 0
  
  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()
  
  # One difference between stacks and queues
  #stack = append
  #queue = insert(0, item)
  
# Tip for exams
# Front of the queue is at the bottom while the bottom of the queue is at the top

# Exam will cover up to lecture 4

# Lecture 5: Linked Lists

