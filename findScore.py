def findScoreSection1():
    scores = []
    Section1 = 0
    with open("score1.txt", "r") as file:
        for line in file:
            score = int(line.strip())
            scores.append(score)
    Section1 = int(sum(scores))
    Section1 = int(((Section1/25)*0.5)*100)
    return Section1

#print("section 1 score: ", findScoreSection1())

def findScoreSection2():
    scores = []
    Section2 = 0
    with open("score2.txt", "r") as file:
        for line in file:
            score = int(line.strip())
            scores.append(score)
    Section2 = int(sum(scores))
    Section2 = int(((Section2/30)*0.3)*100)
    #print("Section2:", Section2)
    return Section2

#print("section 2 score: ", findScoreSection2())

def findScoreSection3():
    scores = []
    Section3 = 0
    with open("score3.txt", "r") as file:
        for line in file:
            score = int(line.strip())
            scores.append(score)
    Section3 = int(sum(scores))
    Section3 = int(((Section3/20)*0.2)*100)
    #print("Section2:", Section2)
    return Section3

#print("section 3 score: ", findScoreSection3())

def printScore1():
    with open("scores.txt", "a") as file:
        file.write(str(findScoreSection1()) + "\n")

def printScore2():
    with open("scores.txt", "a") as file:
        file.write(str(findScoreSection2()) + "\n")

def printScore3():
    with open("scores.txt", "a") as file:
        file.write(str(findScoreSection3()) + "\n")

def findtotalScores():
    scores = []
    Section = 0
    with open("scores.txt", "r") as file:
        for line in file:
            score = int(line.strip())
            scores.append(score)
    Section = int(sum(scores))
    #print("Section2:", Section2)
    return Section
#clear codes

def clear1():
    with open("score1.txt", "w") as file:
        pass

def clear2():
    with open("score2.txt", "w") as file:
        pass

def clear3():
    with open("score3.txt", "w") as file:
        pass

def clear():
    with open("scores.txt", "w") as file:
        pass


