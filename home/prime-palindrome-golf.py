# for code golf
golf=lambda n:[i for i in range(2,10**5) if str(i)==str(i)[::-1] and not any(not i%a for a in range(2,i)) if i>n][0]

print golf(2) == 3
print golf(13) == 101
print golf(101) == 131
