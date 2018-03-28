n = 0
x = 0
y = 0

list1 = []

n = input("Enter: ")

n = n-1


while True:
    if n % 5 == 0 or n % 3 ==0:
        
        list1.append(n)

    n = n-1
    if not n > 1:
        break



for n in list1:
    sum = sum(list1)

    print sum
