# Strongly advised to use else in the recursion (more control over return value)

# Q2

def reverse_int_q2(n):
  if n == 0:
    return n
  else:
  #n % 10, 
  #n % 100 // 10, 
  #n // 100
    return n % 10 * reverse_int_q2(n - 1)
  
def q_2s(s):
  if len(s) == 1:
    return s
  else:
    return s[-1] + str(q_2s(s[:len(s) - 1]))
# Non string way

import math

"""n = 0
def q_2(n, result=0, digits=math.log(n, 10)):
  result += (n % 10) * digits
  if n // 10 == 0:
    return result
  else:
    return q_2(n // 10, result, digits)"""
  
# Lecturer's Solution

def reverse_integer(n, rev=0):
  if n == 0:
    return rev
  else:
    rev = (rev * 10) + (n % 10)
    return reverse_integer(n // 10, rev)


#print(reverse_int_q2(123))
#print(q_2(123))
#print(reverse_integer(123456))