#Left Beehind
sweet = []
sour = []
a = 1
b = 1

while a != 0 and b != 0:
    
    a, b = raw_input().split()
    a, b = [int(a), int(b)]

    sweet.append(a)
    sour.append(b)
    
for x in range(0, len(sweet)-1):
    if sweet[x] + sour[x] == 13:
         print "Never speak again."
    elif sour[x] > 1000 or sour[x] < 0 or sweet[x] < 0 or sweet[x] > 1000:
        break
    elif sweet[x] > sour[x]:
        print "To the convention."
    elif sweet[x] < sour[x]:
        print "Left beehind."
    elif sweet[x] == sour[x]:
        print "Undecided."
            
