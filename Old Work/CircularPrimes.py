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

total = 0

for num in range(1000001):
    num = str(num)
    if len(num) != 1:
        primes = []
        test = []
        while len(num) > len(primes):
            primes.append(0)
            test.append(1)
        
        for y in range(len(num)):
            tempNum = ''
            for x in range(0,len(num)):
                if x + 1 == len(num):
                    x = 0
                else:
                    x = x + 1
                tempNum += num[x]
            if isprime(tempNum):
                primes[y] = 1
            num = tempNum

        if primes == test:
            total += 1
    else:
        if isprime(num):
            total += 1
print(total)
