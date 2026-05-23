class Character():
    #PRIVATE Name : STRING
    #PRIVATE XCoordinate : INTEGER
    #PRIVATE YCoordinate : INTEGER

    def __init__(self, namep, xcp, ycp):
        self.__Name = namep
        self.__XCoordinate = xcp
        self.__YCoordinate = ycp
    
    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate  
    
    def ChangePosition(self, XChange, YChnage):
        self.__XCoordinate+=XChange
        self.__YCoordinate+=YChnage

CharactersArray = []

try:
    myfile = open("Characters.txt")

    for ch in range(10):
        tname = myfile.readline().strip()
        tx = int(myfile.readline())
        ty = int(myfile.readline())
        CharactersArray.append(Character(tname, tx, ty))


    myfile.close()
except:
    print("File not found")

found = False
index = 0

while not found:
    inpname = input("Please enter a characters name: ")

    for x in range(10):
        if CharactersArray[x].GetName().lower() == inpname.lower():
            found = True
            index = x


userinp = ''

while not(userinp == 'W' or userinp == 'A' or userinp == 'S' or userinp == 'D'):
    userinp = input("Enter a letter: ")

if userinp == 'W':
    CharactersArray[index].ChangePosition(0,1)
elif userinp == 'A':
    CharactersArray[index].ChangePosition(-1,0)
elif userinp == 'S':
    CharactersArray[index].ChangePosition(0,-1)
elif userinp == 'D':
    CharactersArray[index].ChangePosition(1,0)

print(f"{CharactersArray[index].GetName()} has changed coordinates to X = {CharactersArray[index].GetX()} and Y = {CharactersArray[index].GetY()}")