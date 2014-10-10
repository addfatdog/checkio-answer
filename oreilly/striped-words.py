#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import re


def checkio(text):
    re_str = '[?!;,. ]'
    vowels = 'AEIOUY'
    con = 'BCDFGHJKLMNPQRSTVWXZ'
    count = 0
    words = [i for i in re.split(re_str, text) if i and len(i) != 1]
    for word in words:
        length = len(word) - 1
        ismyword = True
        for i in xrange(length):
            if word[i].upper() in vowels and word[i + 1].upper() \
                in vowels or word[i].upper() in con and word[i
                    + 1].upper() in con or word[i] in string.digits:
                ismyword = False
                break
        if ismyword:
            count += 1
    return count


# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio(u'My name is ...') == 3, 'All words are striped'
    assert checkio(u'Hello world') == 0, 'No one'
    assert checkio(u'A quantity of striped words.') == 1, 'Only of'
    assert checkio(u'Dog,cat,mouse,bird.Human.') == 3, \
        'Dog, cat and human'

			