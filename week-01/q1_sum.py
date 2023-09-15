#!/usr/bin/env python3

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

print(q1_sum([
    [1, 0, 2],
    [5, 5, 7],
    [9, 4, 3]]))