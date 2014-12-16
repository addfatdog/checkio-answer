def count_neighbours(table,x,y):
  count = 0

  def counter(table, x, y, offset_x, offset_y):
    try:
      if x + offset_x >= 0 and y + offset_y >= 0:
        cell = table[x + offset_x][y + offset_y]
        if cell == 1:
          return 1
    except Exception:
      return 0

    return 0
  
  offset = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for nums in offset:
    count += counter(table, x, y, nums[0], nums[1])

  return count
