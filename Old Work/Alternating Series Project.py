#Alternating Series Program
#Hunter Locke

import math

sel = 0

def function(n):
    x = (math.pow(-1,n)*n)/(math.pow((n+1),2))
    return x

while sel != -1:
    sum = 0
    terms = input("Please enter the number of terms you wish to be used to approximate the sum: ")

    list = []

    for x in range (1,terms + 1):
        list.append(function(x))
    for y in list:
        sum += y

    bound1 = sum - math.fabs(function(terms+1))
    bound2 = sum + math.fabs(function(terms+1))

    print 
    print "**************************************************************************"
    print "The partial sum of " + str(terms) + " terms is " + str(sum)
    print "The error is " + str(math.fabs(function(terms+1)))
    print "The interval of the actual sum is (" + str(bound1) + ", " + str(bound2) + ")"
    print "**************************************************************************"
    print 
