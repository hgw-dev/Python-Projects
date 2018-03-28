


















def poker(line):
    score1 = 0
    score2 = 0
    line = line.replace(' ','')
    p1 = list(line[:10])
    p2 = list(line[10:])
    
    hand1a = {'C': 0,'S':0,'H':0,'D':0}
    hand1b = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for cards in range(1,len(p1),2):
        hand1a[p1[cards]] += 1
    for cards in range(0,len(p1),2):
        if p1[cards].isdigit():
            hand1b[int(p1[cards]) - 2] += 1
        elif p1[cards] == 'J':
            hand1b[9] += 1
        elif p1[cards] == 'Q':
            hand1b[10] += 1
        elif p1[cards] == 'K':
            hand1b[11] += 1
        elif p1[cards] == 'A':
            hand1b[12] += 1
    
    print(hand1b)
    score1 = max([i for i in range(len(hand1b)) if hand1b[i] != 0]) + 1
    score1 = max([i for i in range(len(hand1b)) if hand1b[i] == 2]) + 13
    score1 = max([i for i in range(len(hand1b)) if hand1b[i] == 3]) + 26
   
    print(score1)



test = '5H 5C 6S 7S KD 2C 3S 8S 8D TD'
poker(test)




'''
file = open('poker.txt')
for line in file:
    poker(line)
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    