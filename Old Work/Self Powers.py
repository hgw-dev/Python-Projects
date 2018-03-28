n = input("Enter: ")
p = 0
stuff=[]

while True:
    p += 1
    stuff.append(pow(p,p))
    
    
    if p==n:
        break

sum = sum(stuff)
print str(sum)
