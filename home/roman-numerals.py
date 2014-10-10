def checkio(num):
    a_num = range(1, 11) + [50, 100, 500, 1000]
    r_num = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',\
             'L', 'C', 'D', 'M')
    num_dict = (dict(zip(a_num, r_num)))
    res = ''
    if num == 0:
        return ''
    if num in a_num:
        return num_dict[num]
    else:
        str_num = str(num)
        length = len(str_num)
        
        if length == 2:
            first_num = int(str_num[0])
            last_num = int(str_num[1])
            if first_num <= 3:
                res += num_dict[first_num].replace('I', 'X') + \
                       num_dict[last_num]
            elif first_num == 4:
                res += ('XL' + num_dict[last_num])
            elif first_num == 5:
                res += ('L' + num_dict[last_num])
            elif first_num != 9:
                res += ('L' + num_dict[first_num - 5].replace('I', 'X') + num_dict[last_num])
            else:
                res += ('XC' + num_dict[last_num])

        if length == 3:
            first_num = int(str_num[0])
            if first_num <= 3:
                res += num_dict[first_num].replace('I', 'C') + \
                       checkio(int(str_num[1:]))
            elif first_num == 4:
                res += ('CD' + checkio(int(str_num[1:])))
            elif first_num == 5:
                res += ('D' + checkio(int(str_num[1:])))
            elif first_num != 9:
                res += ('D' + num_dict[first_num - 5].replace('I', 'C') + checkio(int(str_num[1:])))
            else:
                res += ('CM' + checkio(int(str_num[1:])))

        if length == 4:
            first_num = int(str_num[0])
            res += ('M' * first_num + checkio(int(str_num[1:])))
            
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'