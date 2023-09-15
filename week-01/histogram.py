#!/usr/bin/env python3

def histogram(lst, symbol):
  for item in lst:
    print(symbol * item)

histogram([6, 2, 15 , 3, 20 , 5], '=' )