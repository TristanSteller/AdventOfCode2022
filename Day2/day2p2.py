totalScore = 0

data = open('data.txt', 'r').readlines()

for line in data:
    if line[0] == "A":
        if line[2] == "X":
            totalScore += 3
        elif line[2] == "Y":
            totalScore += 4
        elif line[2] == "Z":
            totalScore += 8

    elif line[0] == "B":
        if line[2] == "X":
            totalScore += 1
        elif line[2] == "Y":
            totalScore += 5
        elif line[2] == "Z":
            totalScore += 9
            
    elif line[0] == "C":
        if line[2] == "X":
            totalScore += 2
        elif line[2] == "Y":
            totalScore +=6
        elif line[2] == "Z":
            totalScore +=7
            

print(totalScore)