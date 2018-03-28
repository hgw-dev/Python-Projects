a = 2
b = 2
list=[]
h = input("Enter: ")

for a in range(2, h+1):
    for b in range(2,h+1):
        c = pow(a,b)
        list.append(c)

print len(set(list))
print set(list)
