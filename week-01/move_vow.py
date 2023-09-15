#!/usr/bin/env python3

def move_vow(string):
  vowels = []
  consonants = []
  for s in string:
    if s in "aeiouAEIOU":
      vowels.append(s)
    else:
      consonants.append(s)
  return "".join(vowels + consonants)

print(move_vow('This is DCU!'))