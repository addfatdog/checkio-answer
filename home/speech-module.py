#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(num):
    res = ''
    one_num_dict = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety',
        }

        # keys = one_num_dict.keys()

    str_num = str(num)
    if len(str_num) == 1:
        res = one_num_dict[str_num]
    elif len(str_num) == 2:
        if str_num == '00':
            return ''
        if str_num[0] == '1':
            res = one_num_dict[str_num]
        else:
            if str_num[1] == '0':
                res = one_num_dict[str_num]
            else:
                res = one_num_dict[str_num[0] + '0'] + ' ' \
                    + checkio(int(str_num[1]))
    else:
        res = one_num_dict[str_num[0]] + ' ' + 'hundred ' \
            + checkio(int(str_num[1:3]))
        if res.endswith('zero'):
            res = res[0:-5].strip()
    return res.strip()


# Some hints
# Don't forget strip whitespaces at the end of string

# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio(4) == 'four', '1st example'
    assert checkio(133) == 'one hundred thirty three', '2nd example'
    assert checkio(12) == 'twelve', '3rd example'
    assert checkio(101) == 'one hundred one', '4th example'
    assert checkio(212) == 'two hundred twelve', '5th example'
    assert checkio(40) == 'forty', '6th example'