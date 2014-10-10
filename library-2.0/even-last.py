def checkio(array = None):
  if array:
    return array[-1] * sum(array[::2]) 
  return 0
