#!/usr/bin/env python3

class Memories:
  def __init__(self, **kwargs):
    self.items = list(locals().values())[1]

  def remember(self, item):
    if item in self.items:
      return self.items[item]
    else:
      return False



person1 = Memories(name='Tom', age=32, salary=50000)
print(person1.remember('salary'))
print(person1.remember('email'))