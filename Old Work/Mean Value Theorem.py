#Mean Value Theorem Lab
#Hunter Locke
#10.31.14

import math
sel = 0

while sel != 4:
    print
    print "****************************************"
    print "1. x^2-2x"
    print "2. 1/(x+1)"
    print "3. x^1/2"
    print "4. Quit"
    print "****************************************"
    print
    sel= input("Please enter your selection: ")

    if sel == 1:
        left1= input("Please enter the left endpoint of the interval: ")
        right1= input("Please enter the right endpoint of the interval: ")
        print
        
        ysecant1l= pow(left1, 2)-2*left1
        ysecant1r= pow(right1, 2)-2*right1
        sec1= (ysecant1r-ysecant1l)/(right1-left1)
        c1= (sec1+2)/2.00
        print "The value that satisfies the mean value theorem is: " + str(c1)

        ytangent1= pow(c1, 2)-2*c1
        slopetan1= c1*2-2
        print "The equation of the tangent line of the value that satisfies the mean value theorem is y - " +str(ytangent1) + "= " + str(slopetan1) + "(x - " +str(c1) + ")."

        slopesec1= (ysecant1l-ysecant1r)/(left1-right1)*1.00
        print "The equation of the secant line of these endpoints points is y- " +str(ysecant1l) + "= " + str(slopesec1) + " (x - " + str(left1) + ")."

    elif sel == 2:
        left2= input("Please enter the left endpoint of the interval: ")
        right2= input("Please enter the right endpoint of the interval: ")
        print

        if left2 < -1 and right2 > -1 or left2 == -1 or right2 == -1 or left2>-1 and right2 <-1:
            print "This value is not valid for the mean value theorem. Please try again."
        else:

            ysecant2l= 1.00/(left2+1)
            ysecant2r= 1.00/(right2+1)
            sec2= (ysecant2l-ysecant2r)/(left2-right2)
        
            if left2< -1 and right2<-1:
                c2= (pow((-1/sec2),0.5))*(-1)-1
            elif left2>-1 and right2>-1:
                c2= pow((-1/sec2),0.5)-1
            print "The value that satisfies the mean value theorem is: " + str(c2)

            ytangent2= (1/(c2+1))
            slopetan2= (-1/pow((c2+1),2))
            print "The equation of the tangent line of the value that satisfies the mean value theorem is y - " +str(ytangent2) + "= " + str(slopetan2) + " (x - " +str(c2) + ")."

            print "The equation of the secant line of these endpoints is y- " +str(ysecant2l) + "= " +str(sec2) +" (x - " +str(left2) +")."
            

    elif sel == 3:
        left3= input("Please enter the left endpoint interval: ")
        right3= input("Please enter the right endpoint interval: ")
        print

        if left3 < 0 or right3 < 0:
            print "This value is not valid for the mean value theorem. Please try again."
        else:
            ysecant3l= math.sqrt(left3)
            ysecant3r= math.sqrt(right3)
            sec3= (ysecant3r-ysecant3l)/(right3-left3)
            c3= pow((1/(sec3*2.0)),2)
            print "The value that satisfies the mean value theorem is: " + str(c3)

            ytangent3= math.sqrt(c3)
            slopetan3= 1/(2*math.sqrt(c3))
            print "The equation of the tangent line of the value that satisfies the mean value theorem is y - " +str(ytangent3) + "= " + str(slopetan3) + " (x - " +str(c3) + ")."

            print "The equation of the secant line of these endpoints is y- " +str(ysecant3l) + "= " +str(sec3) +" (x - " +str(left3) +")."

    elif sel == 4:
        print "Goodbye"

    else:
        print "Invalid selection. Please try again."
