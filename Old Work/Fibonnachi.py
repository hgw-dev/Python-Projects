a = 0
b = 1
x = 0
list = []
list1=[]

n = input("Enter: ")

while True:
    x = a + b

    if x % 2 ==0:
        list.append(x)
    list1.append(x)
    
    a = b
    b = x

    if not x < n:
        break

print list
#print list1

sum = sum(list)
print sum
