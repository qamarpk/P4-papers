#DECLARE StackVowel : ARRAY[0:100] OF CHAR
#DECLARE ConsonantVowel : ARRAY[0:100] OF CHAR
StackVowel = ["" for x in range(100)] #100 elements of char
StackConsonant = ["" for y in range(100)] #100 elements of char

#DECLARE VowelTop : INTEGER
#DECLARE ConsonantTop : INTEGER
VowelTop = 0 #integer
ConsonantTop = 0 #integer

def PushData(TheLetter):
    global StackConsonant, StackVowel, VowelTop, ConsonantTop

    if TheLetter in ['a', 'e', 'i', 'o', 'u']:          #checking for vowel
        if VowelTop == 100:
            print("The stack is full. Cannot push.")
        else:
            StackVowel[VowelTop] = TheLetter
            VowelTop += 1
        
    else:
        if ConsonantTop == 100:
            print("The stack is full. Cannot push.")
        else:
            StackConsonant[ConsonantTop] = TheLetter
            ConsonantTop += 1


def ReadData():
    try:
        myFile = open("StackData.txt", 'r')

        for char in myFile:
            PushData(char.strip())

        myFile.close()

    except:
        print("Cannot find file.")
    
def PopVowel():
    global StackVowel, VowelTop

    if VowelTop == "0":
        return "No data"
    else:
        VowelTop -= 1
        ReturnData = StackVowel[VowelTop]
        StackVowel[VowelTop] = ''
        return ReturnData

def PopConsonant():
    global StackConsonant, ConsonantTop

    if ConsonantTop == "0":
        return "No data"
    else:
        ConsonantTop -= 1
        ReturnData = StackConsonant[ConsonantTop]
        StackConsonant[ConsonantTop] = ''
        return ReturnData

ReadData()

ltcount = 0
finalword = ""

while ltcount < 5:
    userchoice = input("Enter \"vowel\" or \"consonant\": ")

    if userchoice == "vowel":
        curlet = PopVowel()
    elif userchoice == "consonant":
        curlet = PopConsonant()
    
    if curlet != "No data":
        finalword += curlet
        ltcount += 1
    else:
        print(f"{userchoice} stack is empty. Try again")

print(finalword)
