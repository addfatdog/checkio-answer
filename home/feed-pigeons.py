def checkio(num):
  mins,birds = 0,0
  wheats = [1]*num
  eated_birds = []
  # print eated_birds
  while wheats:
    mins += 1
    for i in range(mins):
      eated_birds.append(False)

   # print "eated_birds before eat", eated_birds

    birds_num = len(eated_birds)

    for i in range(birds_num):
      wheats.pop(0)
      eated_birds[i] = True

      if not wheats:
        break

  # print "After eated", eated_birds
  return eated_birds.count(True)

print checkio(1) == 1
print checkio(2) == 1
print checkio(3) == 2
print checkio(4) == 3
print checkio(5) == 3
print checkio(6) == 3
print checkio(7) == 3
print checkio(8) == 4
print checkio(9) == 5
print checkio(10) == 6
