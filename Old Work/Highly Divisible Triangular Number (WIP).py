def factor(x):
    list = [x]
    for i in range(1, x):
        if x % i == 0:
            list.append(i)
    return sorted(list, key = int, reverse = False)

counter = 0

for z in range(1, 10000000):
    counter += z
    if len(factor(counter))> 500:
        print counter
