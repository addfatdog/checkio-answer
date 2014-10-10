def letter_queue(commands):
  letter_q = []
  for command in commands:
    if command == 'POP' and len(letter_q) == 0:
      pass
    elif command == 'POP' and len(letter_q) >= 1:
      letter_q.pop(0)
    else:
      letter_q.append(command.split(' ')[1])
  return ''.join(letter_q)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"