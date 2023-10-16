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
        self.items = self.items[::-1]
    
    def sort(self, new=[]):
        if len(self.items) == 0:
            return new
        else:
            new.append("test")
            return
    def reverse_first(self, k):
        self.items = self.items[k::-1]

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.items)
    q.reverse_first(1)
    print(q.items)

def q2(n):
    q2_q = Queue()
    for i in range(1, n + 1):
        str = ""
        temp = i
        while temp:
            if temp & 1:
                str = "1" + str
            else:
                str = "0" + str
            temp >>= 1
        q2_q.enqueue(str)
    return q2_q.size()

print("Q2: " + str(q2(16)))
    


# Q3

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

def q3(s):
    newlst = []
    st = Stack()
    for item in s:
      if item != "*":
          st.push(item)
      elif item == "*":
          newlst.append(st.pop())
    return newlst
          
        

print("Q3: " + str(q3("EAS*Y*QUE***ST***IO*N***")))


def q4(s):
    newlst = []
    q4_1 = Queue()
    for item in s:
      if item != "*":
          q4_1.enqueue(item)
      elif item == "*":
          newlst.append(q4_1.dequeue())
    return newlst

print("Q4: " + str(q4("EAS*Y*QUE***ST***IO*N***")))


def q5(s):
    newlst = []
    q5_s = Stack()
    for item in s:
        q5_s.push(item)
    for item in s:
        newlst.append(q5_s.pop())
    return newlst

print("Q5: " + str(q5([1,2,3,4,5])))

def q6(s):
    q6_s = Stack()
    tokens = s.split()
    s = "".join(tokens)
    for item in s:
        if item.isnumeric():
            q6_s.push(float(item))
        else:
            n2 = q6_s.pop()
            n1 = q6_s.pop()
            if item == "*":
                q6_s.push(float(n1) * float(n2))
            if item == "+":
                q6_s.push(float(n1) + float(n2))
            if item == "-":
                q6_s.push(float(n1) - float(n2))
            if item == "^":
                q6_s.push(float(n1) ** float(n2))
    return q6_s.top()


print("Q6: " + str(q6("1432^*+147--+")))