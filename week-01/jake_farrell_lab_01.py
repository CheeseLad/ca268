#!/usr/bin/env python3

#Q1

def q1_sum(lst):
  total = 0
  nums_processed = []
  for n in lst:
    for d in n:
      nums_processed.append(d)
  for digit in nums_processed:
    if digit % 2 == 0:
      total = total + digit

  return total

# To run the code, uncomment the print statement
#print(q1_sum([[1, 0, 2], [5, 5, 7], [9, 4, 3]]))

#Q2

def move_vow(string):
  vowels = []
  consonants = []
  for s in string:
    if s in "aeiouAEIOU":
      vowels.append(s)
    else:
      consonants.append(s)
  return "".join(vowels + consonants)

# To run the code, uncomment the print statement
#print(move_vow('This is DCU!'))

#Q3

class Memories:
  def __init__(self, **kwargs):
    self.items = list(locals().values())[1]

  def remember(self, item):
    if item in self.items:
      return self.items[item]
    else:
      return False

# To run the code, uncomment the print statements
#person1 = Memories(name='Tom', age=32, salary=50000)
#print(person1.remember('salary'))
#print(person1.remember('email'))

# Q4

class Test:
  def __init__(self, subject_name, correct_answers, passing_mark):
    self.subject_name = subject_name
    self.correct_answers = correct_answers
    self.passing_mark = passing_mark

class Student:
  def __init__(self, name):
    self.name = name

  def take_test(self, Test, answers):

    percentage = int(Test.passing_mark.strip("%"))

    count = 0
    for item in Test.correct_answers:
      if item in answers:
        count = count + 1
    
    percent_individual = 100 // len(Test.correct_answers)
    final_grade = count * percent_individual
    if final_grade >= percentage:
      return self.name + " passed the " + Test.subject_name + " test with the score of " + str(float(percentage)) + "%"
    else:
      return self.name + " failed the " + Test.subject_name + " test!"


# To run the code, uncomment the print statements
#paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
#paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
#paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

#stu1 = Student('Tom')
#print(stu1.take_test(paper2, ['1C', '2C', '3D', '4A']))

#stu2 = Student('John')
#print(stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B']))

# Q5

def histogram(lst, symbol):
  for item in lst:
    print(symbol * item)

# To run the code, uncomment the print statement
#histogram([6, 2, 15 , 3, 20 , 5], '=' )

# Q6

def filter_star(dic, num):
  result = {}
  for item in dic:
    if dic[item] == "*" * num:
      result[item] = "*" * num

  if len(result) > 0:
    return result
  else:
    return "No result found!"

# To run the code, uncomment the print statements
#print(filter_star({
#  'Luxury Chocolates': '*****',
#  'Tasty Chocolates': '****',
#  'Big Chocolates': '*****',
#  'Generic Chocolates': '***'
#}, 4))



#print(filter_star({
#  'Luxury Chocolates': '*****',
#  'Tasty Chocolates': '****',
#  'Big Chocolates': '*****',
#  'Generic Chocolates': '***'
#}, 2))