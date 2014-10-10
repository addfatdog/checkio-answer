def checkio(expr):
    a_stack = []
    for i in expr:
        if i in '({[':
            a_stack.append(i)
        elif i in '}])':
            if a_stack == []:
                return False
            else:
                poped = a_stack.pop()
                if poped == '(' and i != ')':
                    return False
                elif poped == '[' and i != ']':
                    return False
                elif poped == '{' and i != '}':
                    return False
    return len(a_stack) == 0

print checkio("((5+3)*2+1)") == True
print checkio("{[(3+1)+2]+}") == True
print checkio("(3+{1-1)}") == False
print checkio("[1+1]+(2*2)-{3/3}") == True
print checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
print checkio("2+3") == True
