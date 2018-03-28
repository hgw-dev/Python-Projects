import math

tel = {}

def fuckNickInTheAss(n,m):
    return n + m + math.sqrt(n*n+m*m)

for a in range(1,500):
    for b in range(1,a):
        g = fuckNickInTheAss(a, b)
        if (g % 1 == 0 and g <= 1000):
            print(str(a) + "    " + str(b) + "    " + str(g))
            if g in tel.keys():
                tel[g] = tel[g] + 1
            else:
                tel[g] = 1 
            
for x in tel:
    print (str(x) + "    " + str(tel[x]))