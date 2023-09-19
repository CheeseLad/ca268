#!/usr/bin/env python3

def sum_q1(input_list):
  tmp = 0
  for sub_list in input_list:
    for item in sub_list:
      if item % 2 == 0:
        tmp = tmp + item
  return tmp

def move_vow(input_str):
  vows = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  tmp_vow = ""
  tmp_others = ""
  for char in input_str:
    if char in vows:
      tmp_vow = tmp_vow + char
    else:
      tmp_others = tmp_others + char

  return tmp_vow + tmp_others


class Memories:
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      setattr(self, k, v)