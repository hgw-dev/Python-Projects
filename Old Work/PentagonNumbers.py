def f(n):
    x = (n*(3*n-1))
    return x

def g(c):
    n = (1 + (1 - 12*c)**(1/2))/(6)
    return n

number = 10000

for x in range(1,number):
    abra = f(x)
    for y in range(x,number):
        kadabra = f(y)
    
        if g(-abra - kadabra).is_integer() == True and g(abra - kadabra).is_integer() == True:
            print(kadabra - abra)

