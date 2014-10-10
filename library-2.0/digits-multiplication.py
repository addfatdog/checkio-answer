def checkio(num):
  return reduce(lambda a,b: a*b, map(lambda s_num: int(s_num) if (s_num!='0') else 1, str(num)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1