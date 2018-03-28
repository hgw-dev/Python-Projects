def count(num):
    result = ''
    if num[0] == '1':
        result += 'one thousand '
    if num[1] != '0':
        result += value(num[1]) + ' hundred '
    if num[0] != '0' or num[1] != '0':
        if num[2] != '0' or num[3] != '0':
            result += 'and '
    if num[2] != '0' and num[2] != '1' :
        if num[2] == '2':
            result += 'twenty'
        elif num[2] == '3':
            result += 'thirty'
        elif num[2] == '4':
            result += 'forty'
        elif num[2] == '5':
            result += 'fifty'
        elif num[2] == '8':
            result += 'eighty'
        else:
            result += value(num[2]) + 'ty'
    if num[2] != '0' and num[2] != '1' and num[3] != '0':
        result += '-'
    if num[2] == '1':
        if num[3] == '0':
            result += 'ten'
        elif num[3] == '1':
            result += 'eleven'
        elif num[3] == '2':
            result += 'twelve'
        elif num[3] == '3':
            result += 'thirteen'
        elif num[3] == '5':
            result += 'fifteen'
        elif num[3] == '8':
            result += 'eighteen'
        else:
            result += value(num[3]) + 'teen'
    if num[2] != '1' and num[3] != '0':
        result += value(num[3])

    result = result.replace('-','')
    result = result.replace(' ','')

    #print(result)
    #print(len(result))
    return len(result)

def value(digit):
    if digit == '1':
        return 'one'
    elif digit == '2':
        return 'two'
    elif digit == '3':
        return 'three'
    elif digit == '4':
        return 'four'
    elif digit == '5':
        return 'five'
    elif digit == '6':
        return 'six'
    elif digit == '7':
        return 'seven'
    elif digit == '8':
        return 'eight'
    elif digit == '9':
        return 'nine'
##n = 1
##while n != 0:
##    num = input('Enter: ')
##    while len(num) < 4:
##        num = '0' + num
##
##    count(num)
##    print()
    

total = 0
for num in range(1001):
    num = str(num)
    while len(num) < 4:
        num = '0' + num
    total += count(num)
print(total)
