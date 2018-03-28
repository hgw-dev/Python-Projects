n=0

stack = [n]
list1 = [pow(2,n)]

list1.remove(1)
stack.remove(0)

if n > -1:
    n = input("Enter: ")

    while True:
        x= pow(2, n)

        list1.append(x)
        stack.append(n)
        n= n-1
         
        if not x > 2:
            break

print stack
print list1


