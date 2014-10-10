def checkio(lists):
  checksum = sum([sum(i) for i in lists])
  if checksum != 0:
    return False
  length = len(lists)
  for i in range(length):
    for j in range(length):
      if lists[i][j] != 0 - lists[j][i]:
        return False
  return True
  

print checkio([[0,  1,  2], [-1, 0, 1], [-2, -1,  0]])
print checkio([[0,  1, 2], [-1, 1, 1], [-2, -1, 0]])
print checkio([[0,  1, 2], [-1, 0, 1], [-3, -1, 0]])
