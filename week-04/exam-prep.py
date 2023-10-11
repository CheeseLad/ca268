#!/usr/bin/env python3

def q1_sum(lst):
  sum = 0
  for item in lst:
    for i in item:
      if i % 2 == 0:
        sum = sum + i
  return sum

#print(q1_sum([
#    [1, 0, 2],
#    [5, 5, 7],
#    [9, 4, 3]
#]))

def move_vow(string):
  vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
  vowel_list = []
  consonant_list = []
  for s in string:
    if s in vowels:
      vowel_list.append(s)
    else:
      consonant_list.append(s)
  return "".join(vowel_list + consonant_list)

#print(move_vow('This is DCU!'))


class Memories:
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      setattr(Memories, k, v)

  def remember(self, item):
    if hasattr(Memories, item):
      return getattr(Memories, item)
    else:
      return False

#person1 = Memories(name='Tom', age=32, salary=50000)
#print(person1.remember('salary'))
#print(person1.remember('email'))

class Test:
  def __init__(self, subject_name, correct_answers, passing_mark):
    self.subject_name = subject_name
    self.correct_answers = correct_answers
    self.passing_mark = passing_mark

class Student(Test):
  def __init__(self, name):
    self.name = name

  def take_test(self, paper, answers):
    score = 0
    passmk = int(paper.passing_mark[:-1])
    for item in answers:
      if item in paper.correct_answers:
        score = score + (1 / len(paper.correct_answers))
    score = int(score * 100)
    if score > passmk:
      print("{} passed the {} test with the score {}%".format(self.name, paper.subject_name, score))
    else:
      print("{} failed the {} test!".format(self.name, paper.subject_name))

paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

stu1 = Student('Tom')
stu1.take_test(paper2, ['1C', '2C', '3D', '4A'])

stu2 = Student('John')
stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B'])

def histogram(lst, char):
  for item in lst:
    print(char * item)

histogram([6, 2, 15 , 3, 20 , 5], '=' )


def filter_star(lst, num):
  new_dict = {}
  for item in lst.items():
    if item[1].count("*") == num:
      new_dict[item[0]] = item[1]

  return new_dict




print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 4))



print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 2))




