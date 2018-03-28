n = 0
p = input("Enter: ")
o = input("Enter: ")
f = 1
stack = [n]
list=[]

for n in range(p, o):
    while not n == 1:
        if n % 2 == 0:
            n = n/2
            
        elif n % 2 != 0:
            n = (3*n)+1

        stack.append(n)
        f += 1

    a = len(stack)
    list.append(a)

print max(list)
print str(f)
