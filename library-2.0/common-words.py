def checkio(stra, strb):
  return ','.join(sorted(list(reduce(lambda a,b: a&b, map(lambda s: set(s), [i.split(',') for i in [stra, strb]])))))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"