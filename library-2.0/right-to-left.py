left_join = lambda word: ','.join(map(lambda a: a.replace('right', 'left'), [i for i in word]))
