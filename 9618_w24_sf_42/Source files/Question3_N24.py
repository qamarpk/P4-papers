
HighScores = [["","",""] for x in range(7)] #2D Array of type string

def ReadData():
    try:
        myfile = open("HighScoreTable.txt", 'r')

        myArray = [[] for x in range(7)]

        for indx in range(7):                               #adding data to my array
            myArray[indx].append(myfile.readline().strip())
            myArray[indx].append(myfile.readline().strip())
            myArray[indx].append(myfile.readline().strip())

        myfile.close()

        return myArray

    except IOError:
        print("File not found.")

def OutputHighScores(myArray):
    for ind in range(7):
        print(f"{myArray[ind][0]} reached level {myArray[ind][1]} with a score of {myArray[ind][2]}")

def SortScores(myArray):
    swap = True
    top = 7

    while swap and top>0:
        swap = False

        for ind in range(0,top-1):
            if int(myArray[ind][1]) < int(myArray[ind+1][1]):
                myArray[ind], myArray[ind+1] = myArray[ind+1], myArray[ind]
                swap = True
        
        top-=1
    
    return myArray

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)