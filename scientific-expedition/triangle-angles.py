import math

def checkio(a, b, c):
    res = [0, 0, 0]
    if not (a+b>c and a+c>b and b+c>a):
        return res
    else:
        cos_A = (b**2 + c**2 - a**2) / (2.0*b*c)
        num1 = int(round(math.degrees(math.acos(cos_A))))
        cos_B = (c**2 + a**2 - b**2) / (2.0*a*c)
        num2 = int(round(math.degrees(math.acos(cos_B))))
        num3 = 180 - num1 - num2
        res = sorted([num1, num2, num3])
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"