def ReadData():
    try:
        LineArray = [] #strings

        filename = input("Please enter the filename: ")

        myfile = open(filename, 'r')

        line = myfile.readline().strip()

        while line != "":       #looping till EOF
            LineArray.append(line)
            line = myfile.readline().strip()

        myfile.close()
        return LineArray

    except IOError:
        print("File not found.")

def SplitData(DataArray):
    RedArray = [] #integer
    GreenArray = [] #integer
    BlueArray = [] #integer
    OrangeArray = [] #integer
    YellowArray = [] #integer
    PinkArray = [] #integer

    for line in DataArray:
        temp = line.split(',')

        if temp[1] == 'red':           #checking for color
            RedArray.append(temp[0])
        elif temp[1] == 'green':
            GreenArray.append(temp[0])
        elif temp[1] == 'blue':
            BlueArray.append(temp[0])
        elif temp[1] == 'orange':
            OrangeArray.append(temp[0])
        elif temp[1] == 'yellow':
            YellowArray.append(temp[0])
        elif temp[1] == 'pink':
            PinkArray.append(temp[0])
    
    StoreData(RedArray, "Red.txt")
    StoreData(GreenArray, "Green.txt")
    StoreData(BlueArray, "Blue.txt")
    StoreData(OrangeArray, "Orange.txt")
    StoreData(YellowArray, "Yellow.txt")
    StoreData(PinkArray, "Pink.txt")

def StoreData(DataToStore, Filename):
    try:
        myfile = open(Filename, 'a')

        for data in DataToStore:
            myfile.write(data + "\n")

        myfile.close()
    
    except:
        print("Error. Not able to add data")

MyArray = ReadData()
SplitData(MyArray)