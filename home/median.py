def checkio(data):
  length = len(data)
  data.sort()
  if length % 2 == 0:
    res = (data[int(length / 2) - 1] + data[int(length / 2)]) / 2.0
  else:
    res = data[int(length / 2)]
  data[0] = res
  return data[0]
