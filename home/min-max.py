def mymin(*args, **kwargs):
  
  keyfun = None
  if kwargs:
    keyfun= kwargs['key']

  items_data = []
  mapped_data = []
  argv_len = len(args)
  if argv_len > 1:
    items_data = [i for i in args]
    mapped_data = map(keyfun, items_data)
  else:
    items_data = [i for i in args[0]]
    mapped_data = map(keyfun, items_data)

  deal_data = zip(items_data, mapped_data)

  index = deal_data[0]
  for i in deal_data:
    if i[1] < index[1]:
      index = i
  return index[0]

print mymin(3, 2) == 2
print mymin("hello") == 'e'
print mymin([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
print mymin(range(-10, 10)) == -10
print mymin(range(-10, 10), key=abs) == 0
print mymin(abs(i) for i in range(-10, 10)) == 0
print mymin({1,2,3,4,1}) == 1

def mymax(*args, **kwargs):
  
  keyfun = None
  if kwargs:
    keyfun= kwargs['key']

  items_data = []
  mapped_data = []
  argv_len = len(args)
  if argv_len > 1:
    items_data = [i for i in args]
    mapped_data = map(keyfun, items_data)
  else:
    items_data = [i for i in args[0]]
    mapped_data = map(keyfun, items_data)

  deal_data = zip(items_data, mapped_data)

  index = deal_data[0]
  for i in deal_data:
    if i[1] > index[1]:
      index = i
  return index[0]

print mymax(3, 2) == 3
print mymax("hello") == 'o'
print mymax([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [3, 4]
print mymax(range(-10, 10)) == 10
print mymax(range(-10, 10), key=abs) == 10
print mymax(abs(i) for i in range(-10, 10)) == 10
print mymax({1,2,3,4,1}) == 4







