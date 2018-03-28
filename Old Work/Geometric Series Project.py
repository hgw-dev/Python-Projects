#Geometric Series
#Hunter Locke

import math
sel = 0

while sel != 3:
    print "-----------------------------------------------------"
    print
    print "***************************************"
    print "1) Infinite Geometric Series"
    print "2) Finite Geometric Series"
    print "3) Quit"
    print "***************************************"

    sel = input("Please enter your selection: ")
    print

    if sel == 1:
        a1 = input("Please enter your desired value for a: ")
        r1 = input("Please enter your desired value for r: ")
        print

        if r1 > 0 and r1 < 1:
            print "The series converges to " + str((a1*1.0)/(1-(r1*1.0))) + "."
        elif r1 > 1 or r1 == 1:
            print "The series diverges."

    elif sel == 2:
        list = []
        sum = 0
        lowbound = input("Please enter the starting index for the summation: ")
        uppbound = input("Please enter the ending index for the summation: ")
        a2 = input("Please enter your desired value for a: ")
        r2 = input("Please enter your desired value for r: ")
        print

        for x in range(lowbound, uppbound + 1):
            partial = a2 * math.pow(r2, x-1)
            list.append(partial)
        for y in list:
            sum += y

        print "The sum of the series is " + str(sum) + "."

    elif sel == 3:
        print "Good-bye!"
        
    else:
        print "Invalid selection. Please try again."
