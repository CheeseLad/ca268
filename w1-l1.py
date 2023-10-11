

#cost = 
#weight = 

#if weight > 2:
#  print("you need to pay 2 euro extra")


#for i in range(10):
#  print(i)


class Students: # Not dynamic

  programme = "DS"
  module = "CA268"
  name = "Jack"

  def gpa(self, mark_a=100, mark_b=100):
    #print("you have gpa 100!")
    print((mark_a+mark_b)/2) # getting average of both

  def fees(self):
    pass

student1 = Students()
student2 = Students()
student3 = Students()

#print(student1.module)
#print(student1.name)
#print(student3.gpa(mark_a=60, mark_b=30))
#print(student2.gpa(mark_a=80, mark_b=55))
#student1.gpa(mark_a=60, mark_b=30)
#Students.gpa(student1, mark_a=60, mark_b=30)

class Students_d(): # Dynamic, the main way
  
  def __init__(self, name, module, programme): # always ran first when class is called
    self.name = name # assign values
    self.module = module
    self.programme = programme
    self.avg_mark = 0

  def gpa_d(self, mark_a, mark_b):
    self.avg_mark = (mark_a+mark_b)/2

students_d1 = Students_d("Tom", "CA268", "DS")
students_d2 = Students_d("Rose", "CA277", "Medical Science")

print(students_d1.programme)
print(students_d2.module)

students_d2.gpa_d(50, 100)
print(students_d2.avg_mark)
