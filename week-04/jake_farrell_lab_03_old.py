#!/usr/bin/env python3

# Q1

def sum_q1(n):
  if n == 0:
    return n
  else:
    return n + sum_q1(n - 1)

# print(sum_q1(4))

# Q2

def reverse_int(num, reverse=0):
  if num == None:
    return reverse
  else:
    #reverse = reverse + (num % 10) * 10
    #return reverse_int(int(str(num)[:-1]), reverse)
    return (num % 10) *10, num % 10, num % 100 // 10, num % 1000 // 100, num % 10000 // 1000

print(reverse_int(1234))



# Q3

def string_reverse(s, reverse=[]):
  if len(s) == 0:
    return "".join(reverse)
  else:
    reverse.append(s[-1])
    return string_reverse(s[:-1], reverse)
  
# print(string_reverse("hello"))

# Q4

def list_reverse(l, reverse=[]):
  if len(l) == 0:
    return reverse
  else:
    reverse.append(l[-1])
    return list_reverse(l[:-1], reverse)
  
# print(list_reverse([1, 2, 3, 4]))

# Q5

def multiply(num1, num2, total=0):
  if num2 == 0:
    return total
  else:
    if num2 > 0:
      total = total + num1
      return multiply(num1, num2 - 1, total)
    else:
      total = total - num1
      return multiply(num1, num2 + 1, total)

# print(multiply(10, 2))
# print(multiply(-51, -4))
# print(multiply(3, 9))

# Q6

def is_heteromecic(num, counter=0):
  if counter * (counter + 1) < num:
    return is_heteromecic(num, counter + 1)
  else:
    return counter * (counter + 1) == num
  
# print(is_heteromecic(110))

# Q7

def string_length(s, count=0):
  try:
    if s[-1] == None:
      return count
    else:
      count = count + 1
      return string_length(s[:-1], count)
  except IndexError:
    return count

# print(string_length("hello"))