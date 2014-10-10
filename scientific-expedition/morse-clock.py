def checkio(timestr):
    numlist = timestr.split(':')
    alist = []
    numlist = ["{:0>2d}".format(int(i)) for i in numlist]
    for i in numlist:
        for c in i:
            alist.append(bin(int(c)))
    res = ''
    res += "{:0>2d}".format(int(alist[0].replace('0b',''))) + ' '
    res += "{:0>4d}".format(int(alist[1].replace('0b', ''))) + ' : '
    res += "{:0>3d}".format(int(alist[2].replace('0b', ''))) + ' '
    res += "{:0>4d}".format(int(alist[3].replace('0b', ''))) + ' : '
    res += "{:0>3d}".format(int(alist[4].replace('0b', ''))) + ' '
    res += "{:0>4d}".format(int(alist[5].replace('0b', '')))
    res = res.replace('1', '-')
    res = res.replace('0', '.')
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"