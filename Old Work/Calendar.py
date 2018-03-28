n = 0
year = input("Please enter the year: ")
while n != -1:

    day = input("Please enter the day of year: ")

    if year % 4 != 0:

        if day >0 and day <32:
            month = 'January'
            if day == 1 or day == 21 or day == 31:
                print str(month) + " the " + str(day) +"st."
            elif day == 2 or day ==22:
                print str(month) + " the " + str(day) +"nd."
            elif day == 3 or day ==23:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."
                
        if day >31 and day < 60:
            month = "February"
            if day == 32 or day == 52:
                print str(month) + " the " + str(day) +"st."
            elif day == 33 or day ==53:
                print str(month) + " the " + str(day) +"nd."
            elif day == 34 or day ==54:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >59 and day< 91:
            month = "March"
            if day == 60 or day == 80 or day == 90:
                print str(month) + " the " + str(day) +"st."
            elif day == 61 or day ==81:
                print str(month) + " the " + str(day) +"nd."
            elif day == 62 or day ==82:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 90 and day <121:
            month = "April"
            if day == 91 or day == 111:
                print str(month) + " the " + str(day) +"st."
            elif day == 92 or day ==112:
                print str(month) + " the " + str(day) +"nd."
            elif day == 33 or day ==113:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 120 and day <152:
            month = "May"
            if day == 121 or day == 141 or day == 151:
                print str(month) + " the " + str(day) +"st."
            elif day == 122 or day ==142:
                print str(month) + " the " + str(day) +"nd."
            elif day == 123 or day ==143:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 151 and day <182:
            month = "June"
            if day == 152 or day == 172:
                print str(month) + " the " + str(day) +"st."
            elif day == 153 or day ==173:
                print str(month) + " the " + str(day) +"nd."
            elif day == 154 or day ==174:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >181 and day < 213:
            month = "July"
            if day == 182 or day == 202 or day == 212:
                print str(month) + " the " + str(day) +"st."
            elif day == 183 or day ==203:
                print str(month) + " the " + str(day) +"nd."
            elif day == 184 or day ==204:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >212 and day <244:
            month = "August"
            if day == 213 or day == 233 or day == 243:
                print str(month) + " the " + str(day) +"st."
            elif day == 214 or day ==234:
                print str(month) + " the " + str(day) +"nd."
            elif day == 215 or day ==235:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >243 and day <274:
            month = "September"
            if day == 244 or day == 264:
                print str(month) + " the " + str(day) +"st."
            elif day == 245 or day ==265:
                print str(month) + " the " + str(day) +"nd."
            elif day == 246 or day ==266:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 273 and day < 305:
            month = "October"
            if day == 274 or day == 294 or day == 304:
                print str(month) + " the " + str(day) +"st."
            elif day == 275 or day ==295:
                print str(month) + " the " + str(day) +"nd."
            elif day == 276 or day ==296:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 304 and day < 335:
            month = "November"
            if day == 305 or day == 325:
                print str(month) + " the " + str(day) +"st."
            elif day == 306 or day ==326:
                print str(month) + " the " + str(day) +"nd."
            elif day == 307 or day ==327:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 334 and day < 366:
            month = "December"
            if day == 335 or day == 355 or day == 365:
                print str(month) + " the " + str(day) +"st."
            elif day == 336 or day ==356:
                print str(month) + " the " + str(day) +"nd."
            elif day == 337 or day ==357:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

    elif year % 4 == 0:
        
        if day >0 and day <32:
            month = 'January'
            if day == 1 or day == 21 or day == 31:
                print str(month) + " the " + str(day) +"st."
            elif day == 2 or day ==22:
                print str(month) + " the " + str(day) +"nd."
            elif day == 3 or day ==23:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."
                
        if day >31 and day < 61:
            month = "February"
            if day == 32 or day == 52:
                print str(month) + " the " + str(day) +"st."
            elif day == 33 or day ==53:
                print str(month) + " the " + str(day) +"nd."
            elif day == 34 or day ==54:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >60 and day< 92:
            month = "March"
            if day == 61 or day == 81 or day == 91:
                print str(month) + " the " + str(day) +"st."
            elif day == 62 or day ==82:
                print str(month) + " the " + str(day) +"nd."
            elif day == 63 or day ==83:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 91 and day <122:
            month = "April"
            if day == 92 or day == 112:
                print str(month) + " the " + str(day) +"st."
            elif day == 93 or day ==113:
                print str(month) + " the " + str(day) +"nd."
            elif day == 34 or day ==114:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 121 and day <153:
            month = "May"
            if day == 122 or day == 142 or day == 152:
                print str(month) + " the " + str(day) +"st."
            elif day == 123 or day ==143:
                print str(month) + " the " + str(day) +"nd."
            elif day == 124 or day ==144:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 152 and day <183:
            month = "June"
            if day == 153 or day == 173:
                print str(month) + " the " + str(day) +"st."
            elif day == 154 or day ==174:
                print str(month) + " the " + str(day) +"nd."
            elif day == 155 or day ==175:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >182 and day < 214:
            month = "July"
            if day == 183 or day == 203 or day == 213:
                print str(month) + " the " + str(day) +"st."
            elif day == 184 or day ==204:
                print str(month) + " the " + str(day) +"nd."
            elif day == 185 or day ==205:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >213 and day <245:
            month = "August"
            if day == 214 or day == 234 or day == 244:
                print str(month) + " the " + str(day) +"st."
            elif day == 215 or day ==235:
                print str(month) + " the " + str(day) +"nd."
            elif day == 216 or day ==236:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day >244 and day <275:
            month = "September"
            if day == 245 or day == 265:
                print str(month) + " the " + str(day) +"st."
            elif day == 246 or day ==266:
                print str(month) + " the " + str(day) +"nd."
            elif day == 247 or day ==267:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 274 and day < 306:
            month = "October"
            if day == 275 or day == 295 or day == 305:
                print str(month) + " the " + str(day) +"st."
            elif day == 276 or day ==296:
                print str(month) + " the " + str(day) +"nd."
            elif day == 277 or day ==297:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 305 and day < 336:
            month = "November"
            if day == 306 or day == 326:
                print str(month) + " the " + str(day) +"st."
            elif day == 307 or day ==327:
                print str(month) + " the " + str(day) +"nd."
            elif day == 308 or day ==328:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

        if day > 335 and day < 367:
            month = "December"
            if day == 336 or day == 356 or day == 366:
                print str(month) + " the " + str(day) +"st."
            elif day == 337 or day ==357:
                print str(month) + " the " + str(day) +"nd."
            elif day == 338 or day ==358:
                print str(month) + " the " + str(day) +"rd."
            else:
                print str(month) + " the " + str(day) +"th."

    elif day == -1:
        print "Goodbye."

    else:
        print "Invalid selection. Please try again."
