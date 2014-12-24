def weak_point(matrix):
  '''find weak point of a matrix'''
  length = len(matrix) - 1
  min_row = length - 1
  min_col = length - 1

  for i in range(length, -1, -1):

    if sum(matrix[i]) <= sum(matrix[min_row]):
      min_row = i
  
  reversed_matrix = map(list, zip(*matrix))

  for i in range(length, -1, -1):

    if sum(reversed_matrix[i]) <= sum(reversed_matrix[min_col]):
      min_col = i

  return [min_row, min_col]

print weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [3, 3]
print weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [1, 2]
print weak_point([[1,1,1],[1,1,1],[1,1,1]])
