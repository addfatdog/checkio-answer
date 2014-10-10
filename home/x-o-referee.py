def checkio(game_status):
  # row
  row = [i[0] for i in game_status if i[0] in 'XO' and i.count(i[0]) == 3]
  if row:
    return row[0]
    # judge by center
  center = game_status[1][1]
  if center in 'XO':
    if [center, game_status[0][2], game_status[2][0]].count(center) == 3:
      return center
    elif [center, game_status[0][0], game_status[2][2]].count(center) == 3:
      return center
    # col
    for i in xrange(0, 3):
      first = game_status[0][i]
      if first in 'XO':
        second = game_status[1][i]
        third = game_status[2][i]
        if [first, second, third].count(first) == 3:
          return first
  return 'D'

print checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
print checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
print checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
