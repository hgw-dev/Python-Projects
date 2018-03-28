list = []
fact = []


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test(a):

    digit = map(int, str(g))
    for x in digit:
        list.append(factorial(x))

    if a == sum(list):
        return True

for g in range(3,10000):
    if test(g) == True:
        print g


