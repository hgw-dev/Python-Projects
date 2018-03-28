#Hunter Locke
#Euler's Method
#2.12.15

import math

counter = 0
step = input("Please enter the number of steps needed: ")
xvalue = input("Please enter the LAST x-value: ")
firstx = input("Please enter the FIRST x-value: ")
firsty = input("Please enter the FIRST y-value: ")
firsty *= 1.0
firstx *= 1.0
print
deltax = (xvalue-firstx)/step

while True:
    firsty = (firstx + firsty)*(deltax)+ firsty
    counter += 1
    firstx += deltax

    if counter == step:
        break

print
print "The matching y-value would be about " + str(firsty)

if (1 + xvalue + firsty) > 0:
    print "The approximation is an underestimate; f''(" + str(xvalue) + ") = " + str(1 + xvalue + firsty) + " > 0"
elif (1 + xvalue + firsty) < 0.:
    print "The approximation is an overestimate; f''(" + str(xvalue) + ") = " + str(1 + xvalue + firsty) + " < 0."
