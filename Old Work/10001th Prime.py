n=0
x = 0
list=[]
n=input("Enter : ")

def isprime(n):
    '''check if integer n is a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

while True:
    n = 1 + n
    if isprime(n) is True:
        list.append(n)

        x +=1

    if x == 10001:
        break

print str(n)
