global DataStored, NumberItems #integer

DataStored = [None for x in range(20)]

def Initialize():
    global DataStored, NumberItems

    UserNumber = int(input("Enter the quantity of numbers to enter: "))

    while UserNumber<1 or UserNumber>20:
        UserNumber = int(input("Invalid Input. Enter again the quantity of numbers to enter: "))

    for CurNum in range(UserNumber):
        DataStored[CurNum] = int(input(f"Please enter {CurNum+1} number: "))
        NumberItems+=1

NumberItems=0
Initialize()
print(DataStored)

def BubbleSort():
    global DataStored, NumberItems

    swap = True
    top = NumberItems-1

    while swap and top>0:
        swap = False

        for index in range(top):
            if DataStored[index] > DataStored[index+1]:
                DataStored[index], DataStored[index+1] = DataStored[index+1], DataStored[index]
                swap = True
        
        top-=1

BubbleSort()
print(DataStored)

def BinarySearch(DataToFind):
    global DataStored, NumberItems
    up = NumberItems-1
    low = 0

    while up>=low:
        mid = (up+low)//2
        if DataStored[mid] == DataToFind:
            return mid
        elif DataStored[mid] > DataToFind:
            up = mid-1
        else:
            low = mid+1
    
    return -1

SearchInt = int(input("Enter integer to search: "))
print(BinarySearch(SearchInt))