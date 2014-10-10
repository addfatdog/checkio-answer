#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(words):
    words_list = words.split(' ')
    length = len(words_list)
    if length < 3:
        return False
    is_word = map(lambda s: s.isalpha(), words_list)
    for i in xrange(0, length - 2):
        if all([is_word[i], is_word[i + 1], is_word[i + 2]]):
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio(u'Hello World hello') == True, 'Hello'
    assert checkio(u'He is 123 man') == False, '123 man'
    assert checkio(u'1 2 3 4') == False, 'Digits'
    assert checkio(u'bla bla bla bla') == True, 'Bla Bla'
    assert checkio(u'Hi') == False, 'Hi'