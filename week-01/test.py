#!/usr/bin/env python3

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


paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

stu1 = Student('Tom')
print(stu1.take_test(paper2, ['1C', '2C', '3D', '4A']))

stu2 = Student('John')
print(stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B']))