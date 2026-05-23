Animal = ["" for x in range(20)]
Colour = ["" for c in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DatatoPush):
    global AnimalTopPointer, Animal
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DatatoPush
        AnimalTopPointer+=1
        return True

def PopAnimal():
    global AnimalTopPointer, Animal
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer-=1
        return ReturnData


def ReadData():
    try:
        AnimalFile = open("AnimalData.txt", 'r')
        
        for name in AnimalFile:
            PushAnimal(name.strip())

        AnimalFile.close()
    except IOError:
        print("Animal file not found.")

    try:
        ColourFile = open("ColourData.txt", 'r')
        
        for name in ColourFile:
            PushColour(name.strip())

        ColourFile.close()
    except IOError:
        print("Colour file not found.")

def PushColour(DatatoPush):
    global ColourTopPointer, Colour
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DatatoPush
        ColourTopPointer+=1
        return True

def PopColour():
    global ColourTopPointer, Colour
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer-=1
        return ReturnData

def OutputItem():
    myAnimal = PopAnimal()
    myColour = PopColour()

    if myAnimal == "":
        PushAnimal(myAnimal)
        print("No colour")
    elif myColour == "":
        PushColour(myColour)
        print("No animal")
    else:
        print(myColour, " ", myAnimal)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
