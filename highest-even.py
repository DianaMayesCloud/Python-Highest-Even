#My first solution: Does not create a new list
def highest_even(li):
  li.sort()
  li.reverse()
  i = 0
  while i < len(li):
    if li[i] %2 == 0:
      print(li[i])
      break
    i += 1
  return li[i]

highest_even([10, 2, 3, 4, 8, 11])


# My second solution: Creates a new list
def highest_even(li):
  even_li = []
  for item in li:
    if item %2 == 0:
      even_li.append(item)
  even_li.sort()
  even_li.reverse()
  for item in even_li:
    return even_li[0]

print(highest_even([10, 2, 3, 4, 8, 11]))

# Andrei's solution: Creates a new list

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))