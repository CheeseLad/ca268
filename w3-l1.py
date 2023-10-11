
a = [1, 2, 3, 4, 5, 6, 7]
q = 3

#n^2 (nested loop)

for i in a:
  for j in a:
    print(i, j)


#n * m (because there is a different amount of elements)

a = [1, 2, 3, 4, 5, 6, 7]
len_a = 6
b = [10, 20, 30, 40, 50, 60, 70]
len_b = 7
q = 3



for i in a:
  for j in a:
    print(i, j)

len_a * len_b

# why didnt we say it's quadratic time complexity (special case of n * m)

# Cubic function (n^3)


a = [1, 2, 3, 4, 5, 6, 7]
len_a = 6
b = [10, 20, 30, 40, 50, 60]
len_b = 6
c = [100, 200, 300, 400, 500, 600]
len_c = 6
q = 3



for i in a:
  for j in a:
    for k in c:
      print(i, j, k)

len_a * len_b * len_c


# The Factorial Function

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
  
# Factorial without recursion

n = 10

i = 1
output = 1
while i < n:
  output = output * i
  i = i + 1
print(output)