def verify_anagrams(first_word, second_word):
    first_word = first_word.replace(' ', '').upper()
    second_word = second_word.replace(' ', '').upper()
    first_length = len(first_word)
    second_length = len(second_word)

    # print 'One', first_word
    # print 'Two', second_word
    
    if first_length != second_length:
      return False
    else:
      for first_char in first_word:
        if second_word.count(first_char) != first_word.count(first_char):
          return False
    return True