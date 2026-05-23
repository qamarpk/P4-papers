from random import randint

ArrayData = [[],[],[],[],[],[],[],[],[],[]]

def OutputArray():
    for row in range(0,10):
        for column in range(0,10):
            if len(str(ArrayData[row][column])) == 1:
                print("0" + str(ArrayData[row][column]), end = " ")
            else:
                print(ArrayData[row][column], end = " ")
        print()


for i in range(0,10):
    for r in range(0,10):
        ArrayData[i].append(randint(1,100))
    
ArrayLength = 10

OutputArray()
print("\n")


for X in range(0,ArrayLength):
    for Y in range(0,ArrayLength-1):
        for Z in range(0, ArrayLength-Y-1):
            if ArrayData[X][Z] > ArrayData[X][Z+1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue

OutputArray()



def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper>= Lower:
        Mid = (Lower + (Upper))//2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    
    return -1

print(BinarySearch(ArrayData, 0, 9, ArrayData[0][4]))
print(BinarySearch(ArrayData, 0, 9, 200))


