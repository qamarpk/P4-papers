from random import randint

global MyArray
MyArray = [] #20 elements of integer

for x in range(20):
    num = randint(0,100)
    while num in MyArray:
        num = randint(0,100)
    MyArray.append(num)

def PrintArray(intarray):
    for num in intarray:
        print(num, end=" ")

def BubbleSort(intarray):
    top = len(intarray)
    swap = True
    while swap == True:
        swap = False

        for x in range(0, top-1):
            if intarray[x] > intarray[x+1]:
                intarray[x], intarray[x+1] = intarray[x+1], intarray[x]
                swap = True

        top-=1

    return intarray 

PrintArray(MyArray)
MyArray = BubbleSort(MyArray)
print("\nSorted")
PrintArray(MyArray)

def RecursiveBinarySearch(intarray, lowerb, upperb, value):
    mid = (upperb+lowerb)//2
    if upperb < lowerb:
        return -1
    elif intarray[mid] == value:
        return mid
    elif value > intarray[mid]:
        return RecursiveBinarySearch(intarray, mid+1, upperb, value)
    elif value < intarray[mid]:
        return RecursiveBinarySearch(intarray, lowerb, mid-1, value)

userinp = int(input("\nEnter Integer: "))
index = RecursiveBinarySearch(MyArray, 0, len(MyArray), userinp) 
if index == -1:
    print("Not found")
else:
    print("Found at position: " + str(index))