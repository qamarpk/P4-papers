class NewRecord:
    def __init__(self, keyp, it1p, it2p):
        self.Key = keyp #INTEGER
        self.Item1 = it1p #INTEGER
        self.Item2 = it2p #INTEGER

HashTable = [] #NewRecord 200 elements
Spare = [] #NewRecord 100 elements]

def Initialise():
    global HashTable, Spare

    HashTable = [-1 for x in range(200)]
    Spare = [-1 for y in range(100)]

def CalculateHash(myKey):
    return (myKey%200)

def InsertIntoHash(AddRecord):
    global HashTable, Spare

    HashValue = CalculateHash(AddRecord.Key)

    if HashTable[HashValue] == -1:
        HashTable[HashValue] = AddRecord
    else:
        endp = 0 
        while Spare[endp] != -1:
            endp+=1
        
        Spare[endp] = AddRecord

def CreateHashTable():
    try:
        myFile = open("HashData.txt")

        for line in myFile:
            line = line.strip().split(",")
            InsertIntoHash(NewRecord(int(line[0]), int(line[1]), int(line[2])))

        myFile.close()
    except:
        print("File not found")

def PrintSpare():
    global Spare

    curin = 0

    while Spare[curin] != -1:
        print(Spare[curin].Key, end = ' ')
        curin+=1

Initialise()
CreateHashTable()
PrintSpare()

