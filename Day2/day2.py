totalScore = 0

offset1 = 64
offset2 = 87


def calculatePoints(a, b):
    score = 0
    char1 = a
    char2 =  b
    score += (ord(char2) - offset2)
    print(ord(char2) - offset2)
    rps1 = ord(char1) - offset1
    rps2 = ord(char2) - offset2
    if rps1 == rps2:
        score += 3
        print("tie")
    elif (rps1 == 1  and rps2 ==2) or (rps1 == 2  and rps2 == 3) or (rps1 == 3 and rps2 ==1):
        print("win")
        score += 6
    else:
        print("loss")
    return score


data = open('data.txt', 'r').readlines()

#print(calculatePoints("B", "Y"))


for line in data:
    print(totalScore)
    totalScore += calculatePoints(line[0], line[2])

print(totalScore)

