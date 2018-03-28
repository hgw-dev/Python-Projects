n = 0
year = input("Please enter the year: ")
while n != -1:

    day = input("Please enter the day of year: ")

    if year % 4 != 0:

        if day >0 and day <32:
            month = 'January'

        elif day >31 and day < 60:
            month = "February"

        elif day >59 and day< 91:
            month = "March"

        elif day > 90 and day <121:
            month = "April"

        elif day > 120 and day <152:
            month = "May"

        elif day > 151 and day <182:
            month = "June"

        elif day >181 and day < 213:
            month = "July"
     
        elif day >212 and day <244:
            month = "August"
      
        elif day >243 and day <274:
            month = "September"

        elif day > 273 and day < 305:
            month = "October"

        elif day > 304 and day < 335:
            month = "November"
 
        elif day > 334 and day < 366:
            month = "December"

        if month == 'February':
            while True:
                day = day - 31
                if not day > 29:
                    break

        elif month == "April" or month == "June" or month == "September" or month == "November":
            while True:
                day = day - 30
                if not day > 31:
                    break            
    
    elif year % 4 == 0:
        if day >0 and day <32:
            month = 'January'
      
        elif day >31 and day < 60:
            month = "February"
      
        elif day >59 and day< 91:
            month = "March"
          
        elif day > 90 and day <121:
            month = "April"
        
        elif day > 120 and day <152:
            month = "May"
 
        elif day > 151 and day <182:
            month = "June"
  
        elif day >181 and day < 213:
            month = "July"

        elif day >212 and day <244:
            month = "August"

        elif day >243 and day <274:
            month = "September"
     
        elif day > 273 and day < 305:
            month = "October"

        elif day > 304 and day < 335:
            month = "November"
 
        elif day > 334 and day < 366:
            month = "December"

    if day == 1 or day == 21 or day == 31:
        print str(month) + " the " + str(day) +"st."
    elif day == 2 or day ==22:
        print str(month) + " the " + str(day) +"nd."
    elif day == 3 or day ==23:
        print str(month) + " the " + str(day) +"rd."
    else:
        print str(month) + " the " + str(day) +"th."
