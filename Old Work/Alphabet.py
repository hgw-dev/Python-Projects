n = 0

while n!=-1:
    
    word = 'abcdefghijklmnopqrstuvwxyz'
    n = input("Enter: ")
    z = n/26
    
    if n < 26 and n > 0 or n==26:
        print word[n-1]
        print "The sequence did not repeat itself."
        print

    elif n <1:
        print "Invalid selection. Please try again."
        print
        
    else:
        while True:
            n= n - 26
            if not n >26:
                break
            
        print word[n-1]

        if z == 1:
            print "The sequence repeated " + str(z) + " time."
        else:
            print "The sequence repeated " + str(z) + " times."
        print      
