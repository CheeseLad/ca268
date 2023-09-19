
class Person:

  def __init__(self, name):
    self.name = name
    self.flag_student = False

  def get_name(self):
    return self.name
  
  def is_student(self):
    if self.flag_student:
      return True
    else:
      return False
  
class Student(Person):

  def is_student(self):
    return True
  
def Subclass(obj):
  obj.name
  # can't instantiate a class based on an object


person1 = Person("Tom")
print(person1.is_student()) # False
person1.flag_student = True
print(person1.is_student()) # True
setattr(student1, "email", "adad2@mail.dcu.ie")

#student1 = Student("Jack")
#print(student1.is_student())