palid = []

for n in range(99, 1000):
    for x in range(99, 1000):
        c = x*n
        c= str(c)
        if c[0]==c[-1] and c[1]==c[-2] and c[2]==c[-3]:
            palid.append(c)

print sorted(palid, key=int, reverse=False)
