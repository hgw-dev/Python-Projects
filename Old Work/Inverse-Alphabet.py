counter = 0
list = []
x = 0
over_count = 0
word = 'abcdefghijklmnopqrstuvwxyz'

while x != -1:
    cap = input("Cap Value: ")

    while counter != cap:
        n = raw_input("Enter: ")
        list.append(word.index(n)+1)
        counter = counter + 1

    summ = sum(list)
    counter = 0
    over_count = over_count + 1
    print over_count*summ
