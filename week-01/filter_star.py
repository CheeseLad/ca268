
def filter_star(dic, num):
  result = {}
  for item in dic:
    if dic[item] == "*" * num:
      result[item] = "*" * num

  if len(result) > 0:
    return result
  else:
    return "No result found!"

print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 4))



print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 2))