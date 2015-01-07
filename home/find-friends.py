def check_connection(connections, person1, person2):
  
  firend_set = []

  paris = map(lambda conn: conn.split('-'), connections)
  length_of_pairs = len(paris)

  firend_set.append(paris[0])

  for index in range(1, length_of_pairs):
    lenght_of_set = len(firend_set)
    not_in_set = True
    in_which_set = []

    for count in range(lenght_of_set):

      if paris[index][0] in firend_set[count] and \
         paris[index][1] not in firend_set[count]:
        firend_set[count].append(paris[index][1])

        in_which_set.append(count)

        not_in_set = False
      elif paris[index][1] in firend_set[count] and \
         paris[index][0] not in firend_set[count]:
        firend_set[count].append(paris[index][0])
        not_in_set = False

        in_which_set.append(count)

      elif paris[index][1] in firend_set[count] and \
         paris[index][0] in firend_set[count]:
        not_in_set = False
        
        in_which_set.append(count)

        continue

    if not_in_set:
      firend_set.append(paris[index])
    else:
      if len(in_which_set)!=1:
        many_list = map(set, [firend_set[i] for i in in_which_set])
        firend_set.append(list(set(reduce(lambda a, b : a | b, many_list))))  

  print firend_set

  for every in firend_set:
    if person1 in every and person2 in every:
      print every
      return True

  return False

print check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
print 
print check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
print 
print check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
print
print check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True
print
print check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),
  "dr101","mr99")
