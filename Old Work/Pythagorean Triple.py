def triplet(n):
    if n > 0:
        for a in range(1, n-1):
            for b in range(a+1, n):
                for c in range(b+1, n+1):
                    if a*a + b*b == c*c and a + b + c == n:
                        print (a,b,c)
                        print a*b*c
    
n = input("Enter: ")
triplet(n)
