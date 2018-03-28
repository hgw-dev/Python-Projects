n = input("Enter: ")
a = 1
list= []

for x in range(n, 1, -1):
    list.append(x)
    a = a *x


print str(a)
print map(int, str(a))
print sum(map(int,str(a)))
