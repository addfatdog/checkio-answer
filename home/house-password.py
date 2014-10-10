import string

def checkio(data):
    condtions = [False] * 4
    if len(data) >= 10:
        condtions[0] = True
    for i in data:
        if i in string.digits:
            condtions[1] = True
        elif i in string.ascii_lowercase:
            condtions[2] = True
        elif i in string.ascii_uppercase:
            condtions[3] = True
    return all(condtions)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"