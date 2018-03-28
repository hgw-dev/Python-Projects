a = 0
b = 1
x = 0
g = 1
list = []

n = input("Enter: ")

while True:
    x = a + b
    
    a = b
    b = x

    g += 1
    list.append(g)

    if len(map(int, str(x)))==n:
        break

print max(list)
print x
