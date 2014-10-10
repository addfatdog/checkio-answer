def checkio(data):
  data = [i for i in data if data.count(i) != 1]
  return data

print checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
print checkio([1, 2, 3, 4, 5]) == []
print checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
print checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
