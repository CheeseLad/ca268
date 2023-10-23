#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

    def find(self, target_data):
        current = self
        while current is not None:
            if current.data == target_data:
                return current
            current = current.next
        return None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    """def add_to_first(self, item):
        new_node = Node(item)
        current_node = self.head.next
        current_data = self.head.data
        new_node.head.n = cu
        self.head = current.next"""

    """def find(self, looking):
      current = self.head
      while current.data != looking:
          if current.data == looking:
              return current
              break
          else:
              current = current.next"""
  

even_numbers_list = LinkedList()
for number in range(0, 101):
    if number % 2 == 0:
      even_numbers_list.append(number)

even_numbers_list.display()
#even_numbers_list.add_to_first("test")
#even_numbers_list.display()


head = Node("Dublin")
another_node = Node("Galway")
head.next = another_node
a_third_node = Node("Cork")
another_node.next = a_third_node

result = head.find("Galway")
print(result.data)

def reverse(ll):
    current = ll.head
    test = []
    newll = LinkedList()
    while current is not None:
        prev = current.data
        test.append(prev)
        current = current.next
    for item in test[::-1]:
        newll.append(item)
        
    #print(newll.display())
    

reverse(even_numbers_list)

def swap_pairs(ll):
    print(ll.head.data)

q4 = LinkedList()
q4.append(2)
q4.append(1)
q4.append(4)
q4.append(3)
#swap_pairs(head)


def remove_nth_from_end(head, n):
    if not head:
        return None

    # Initialize two pointers, first_ptr and second_ptr
    first_ptr = head
    second_ptr = head

    # Move the second_ptr n nodes ahead
    for _ in range(n):
        if not second_ptr:
            return head  # n is greater than the number of nodes
        second_ptr = second_ptr.next

    # If second_ptr has reached the end, remove the head node
    if not second_ptr:
        return head.next

    # Move both pointers until second_ptr reaches the end
    while second_ptr.next:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    # Remove the nth node
    first_ptr.next = first_ptr.next.next

    return head

# Example usage
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print("Original Linked List:")
my_list.display()

n = 3

my_list.head = remove_nth_from_end(my_list.head, n)

print(f"Linked List after removing {n}th node from the end:")
my_list.display()