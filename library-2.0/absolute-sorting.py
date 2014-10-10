def checkio(num_list):
  num_list = list(num_list)
  num_list.sort(cmp = lambda a,b:cmp(abs(a), abs(b)))
  return num_list
