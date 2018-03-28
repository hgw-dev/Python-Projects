# Hunter Williams (hl3xb)
import pyperclip
a_to_r = ["I", "V", "X", "L", "C", "D", "M"]
arabic = [1,5,10,50,100,500,1000]
occur = [0,0,0,0,0,0,0]

def print_rom(number):
    pos = 0
    s = ""
    while pos <= 6:
        value = occur[pos]
        if value == 4 and pos % 2 == 0 and occur[pos + 1] == 1 :
            s += a_to_r[pos+2]
            s += a_to_r[pos]
            pos += 1
        elif value == 4:
            s += a_to_r[pos+1]
            s += a_to_r[pos]
        else:
            s += value*a_to_r[pos]
        pos += 1
    print("In roman numerals, " + str(number) + " is " + s[::-1])
    pyperclip.copy(s[::-1])

def convert(num, step):
    value = arabic[step]
    for i in range(0,5):
        if num - value*i >= 0 and num - value*(i+1) < 0:
            return i
    return i

def arabic_to_roman(number):
    number = int(number)
    store = number
    if number >= 1 and number <=  3999:
        for x in range(6,-1,-1):
            occur[x] = convert(number,x)
            number = number - occur[x]*arabic[x]

        print_rom(store)
    else:
        print("Input must be between 1 and 3999")

def roman_to_arabic(number):
    num = list(number)
    sum_num = 0
    for x in num:
        sum_num += arabic[a_to_r.index(x)]
    for i in range(0,len(num)-1):
        if a_to_r.index(num[i]) < a_to_r.index(num[i+1]):
            sum_num -= 2*arabic[a_to_r.index(num[i])]
        
    print("In arabic numerals, " + str(number) + " is " + str(sum_num))
    pyperclip.copy(str(sum_num))

def main():    
    number = input("Enter an integer: ")
    temp = list(number)
        
    if temp[0] in a_to_r:
        roman_to_arabic(number)
    else:
        arabic_to_roman(number)
    print()

n = -1
while n != 0:
    main()
