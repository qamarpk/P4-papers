WordArray = []
NumberWords = -1

def Play():
    global WordArray, NumberWords

    correctcount = 0

    print(f"The main word is \"{WordArray[0]}\" and there are {NumberWords} answers.")

    userword = input("Enter your answer (or no to stop): ").lower()

    while userword != "no":
        
        found = False

        for curind in range(1, len(WordArray)):
            if WordArray[curind] == userword:
                found = True
                WordArray[curind] = ""
        
        if found:
            print("Word entered is an answer.")
            correctcount+=1
        else:
            print("Word entered is not an answer.")
        
        userword = input("Enter your answer: ").lower()
    
    percentage = round((correctcount/NumberWords) * 100)
    print(f"You entered {percentage}% of possible answers.")

    print("You missed: ")
    for x in range(1, len(WordArray)):
        if WordArray[x] != "":
            print(WordArray[x], end=", ")


def ReadWords(Filename):
    global WordArray, NumberWords
    try:
        
        myfile = open(Filename, 'r')
        word = myfile.readline().strip()

        while word != "":
            WordArray.append(word)
            word = myfile.readline().strip()
            NumberWords +=1
        
        myfile.close()
    except IOError:
        print("File not found.")
    
    Play()
    


userchoice = input("Enter \"easy\", \"medium\" or \"hard\" for the game difficulty: ").lower()

if userchoice == "hard":
    ReadWords("Hard.txt")
elif userchoice == "medium":
    ReadWords("Medium.txt")
elif userchoice == "easy":
    ReadWords("Easy.txt")

