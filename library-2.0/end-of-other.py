def checkio(words):
    words = list(words)
    length = len(words)
    if length == 1:
        return False
    if length == 2:
        if words[0].endswith(words[1]) or words[1].endswith(words[0]):
            return True
        print words[0]
        return True
    for i in xrange(length):
        for j in xrange(i + 1, length):
            if words[i].endswith(words[j]) or words[j].endswith(words[i]):
                return True 
    return False