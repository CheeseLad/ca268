

#cost = 
#weight = 

#if weight > 2:
#  print("you need to pay 2 euro extra")


#for i in range(10):
#  print(i)


class Students:

  programme = "DS"
  module = "CA268"
  name = "Jack"

  def gpa(self, mark_a=100, mark_b=100):
    #print("you have gpa 100!")
    print((mark_a+mark_b)/2)

student1 = Students()
student2 = Students()
student3 = Students()

#print(student1.module)
print(student1.name)
print(student3.gpa(mark_a=60, mark_b=30))
print(student2.gpa(mark_a=80, mark_b=55))
  
