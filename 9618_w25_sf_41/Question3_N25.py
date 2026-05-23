class Record():
    #DECLARE Key : Integer
    #DECLARE Data : String
    def __init__(self, keyp, datap):
        self.Key = keyp
        self.Data = datap

def InitialiseHashTable():
    global HashTable 
    HashTable = [[None for x in range(10)] for y in range(100)] #10x100 of type Record

def Hash(Key):
    return Key % 100

def InsertData(NewRecord):
    Index = Hash(NewRecord.Key)
    for ind2 in range(10):
        if HashTable[Index][ind2] == None:
            HashTable[Index][ind2] = NewRecord
            break

def ReadData():
    try:
        hashfile = open("HashTableData.txt", 'r')
        line = hashfile.readline()
        while line != "":
            line = line.strip().split(",")
            InsertData(Record(int(line[0]), line[1]))
            line = hashfile.readline()

        hashfile.close()
    except:
        print("File Not Found")
    
def GetRecord(Key):
    Index = Hash(Key)
    for ind2 in range(10):
        if HashTable[Index][ind2] != None:
            if HashTable[Index][ind2].Key == Key:
                return HashTable[Index][ind2].Data  
    return "Not found"

InitialiseHashTable()
ReadData()

for i in range(5):
    userinp = int(input("Please enter key field to search for: "))
    print(GetRecord(userinp))