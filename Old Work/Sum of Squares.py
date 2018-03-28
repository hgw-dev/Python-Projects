x = 0
y = 0
list=[]
stack=[]
x = input("Enter: ")

while True:
    x = 1 + x
    list.append(x)


    y = pow(x,2)
    stack.append(y)
    if not x < 100:
        break

pow = pow(sum(list),2)
print pow
    
sum = sum(stack)
print sum

diff= pow - sum
print str(diff)

print list
print stack 
