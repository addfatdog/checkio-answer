from datetime import datetime as date
days_diff = lambda d1, d2 : abs((date(d1[0], d1[1], d1[2])-date(d2[0], d2[1], d2[2])).days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238