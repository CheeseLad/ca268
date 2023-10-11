#!/usr/bin/env python3

# Q1

def sum_q1(n):
  if n == 0:
    return n
  else:
    return n + sum_q1(n - 1)
  
#print(sum_q1(6))

# Q2

def reverse_integer(n, rev=0):
  if n == 0:
    return rev
  else:
    rev = (rev * 10) + (n % 10)
    return reverse_integer(n // 10, rev)

#print(reverse_integer(123456))

# Q3

def string_reverse(str, rev=[]):
  if len(str) == 0:
    return "".join(rev)
  else:
    rev.append(str[-1])
    return string_reverse(str[:-1], rev)
  
#print(string_reverse("hello"))

# Q4

def list_reverse(str, rev=[]):
  if len(str) == 0:
    return rev
  else:
    rev.append(str[-1])
    return list_reverse(str[:-1], rev)
  
#print(list_reverse([1, 2, 3, 4]))

# Q5

def multiply(n, m, count=0, sum=0):
  if count == m:
    return sum
  else:
    if m > 0:
      sum = sum + n
      return multiply(n, m, count + 1, sum)
    else: 
      sum = sum - n
      return multiply(n, m, count - 1, sum)

  
#print(multiply(10, 2))
#print(multiply(-51, -4))
#print(multiply(3, 9))

# Q6

def is_heteromecic(n, i=0):
  if i * (i + 1) < n:
    return is_heteromecic(n, i + 1)
  else:
    return i * (i + 1) == n

#print(is_heteromecic(110))

# Q7

def string_length(str, count=0):
  if str == "":
    return count
  else:
    return string_length(str[1:], count + 1)

#print(string_length("testing"))