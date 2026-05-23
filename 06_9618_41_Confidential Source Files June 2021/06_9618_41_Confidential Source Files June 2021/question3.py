class TreasureChest:
    #Private question : String
    #Private answer : Integer
    #Private points : Integer

    def __init__(self, questioP, answerP, pointsP):
        self.question = questioP
        self.answer = int(answerP)
        self.points = int(pointsP)

    def getQuestion(self):
        return(self.question)
    
    def checkAnswer(self, userans):
        if userans == self.answer:
            return True
        else:
            return False
    
    def getPoints(self, noattempts):
        if noattempts == 1: return self.points
        elif noattempts == 2: return self.points//2
        elif noattempts == 3 or noattempts == 4: return self.points//4
        else: return 0

arrayTreasure = []

def readData():
    filename = "TreasureChestData.txt"
    try:
        myfile = open(filename, 'r')
        for x in range(0,5):
            q = myfile.readline().strip()
            a = myfile.readline().strip()
            p = myfile.readline().strip()
            arrayTreasure.append(TreasureChest(q,a,p))
        myfile.close()

    except FileNotFoundError:
        print("File was not found")

readData()
userinp = int(input("Choose a question no between 1 and 5: "))-1
while userinp  not in range(0,5):
    print("try again")
    userinp = int(input("Choose a question no between 1 and 5: "))-1

print(arrayTreasure[userinp].getQuestion())

userans = int(input("Type the answer: "))

count = 1
result = arrayTreasure[userinp].checkAnswer(userans)

while result == False:
    userans = int(input("That was wrong! Type another answer: "))
    result = arrayTreasure[userinp].checkAnswer(userans)
    count+=1

print(arrayTreasure[userinp].getPoints(count))