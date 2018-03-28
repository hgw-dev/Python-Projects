import re
            
    
for a in range(10,99):
    for b in range(a + 1,100):
        num = str(a)
        den = str(b)
        c = a/b
        
        digA = num[0]
        digB = num[1]
        
        if (digA in den and '0' not in digA):
            num = re.sub(digA,"",num,count = 1)
            den = re.sub(digA,"",den,count = 1)
            if ('0' not in den):
                if (int(num)/int(den) == c):
                    print(str(a) + "/" + str(b))
        elif (digB in den and '0' not in digB):
            num = re.sub(digB,"",num,count = 1)
            den = re.sub(digB,"",den,count = 1)
            if ('0' not in den):
                if (int(num)/int(den) == c):
                    print(str(a) + "/" + str(b))
    
        
        
        