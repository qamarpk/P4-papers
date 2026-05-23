global DataArray
DataArray = [0 for x in range(100)]

def ReadFile():
    try:
        myfile = open("IntegerData.txt")
        for x in range(100):
            DataArray[x] = int(myfile.readline().strip())
        
        myfile.close()

    except IOError:
        print("File not found")

def FindValues():
    mynum = int(input("Please enter number to search: "))

    while mynum > 100 or mynum < 0 :
        mynum = int(input("Number is invalid. Please enter number again to search: "))

    count = 0

    for curnum in DataArray:
        if curnum == mynum: count+=1
    
    return count

ReadFile()
print("Number of repetitions is ", FindValues())

def BubbleSort():
    global DataArray
    top = 100
    swap = True

    while swap == True:
        swap = False

        for index in range(top-1):
            if DataArray[index] > DataArray[index+1]:
                DataArray[index], DataArray[index+1] = DataArray[index+1], DataArray[index]
                swap = True
        
        top-=1
    
BubbleSort()
print(DataArray)