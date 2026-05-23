global NumberArray #integers
NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2

    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    
    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem = CheckItem -1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

newarr = RecursiveInsertion(NumberArray , len(NumberArray))
print("Recursive")
print(newarr)

NumberArray = [100, 85, 644, 22, 15, 8, 1]


def IterativeInsertion(IntegerArray, NumberElements):
    while NumberElements>0:
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2

        LoopAgain = True
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] <= LastItem:
                LoopAgain = False
        
        while LoopAgain:
            IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
            CheckItem = CheckItem -1
            if CheckItem < 0:
                LoopAgain = False
            else:
                if IntegerArray[CheckItem] <= LastItem:
                    LoopAgain = False
    
        IntegerArray[CheckItem + 1] = LastItem

        NumberElements-=1

    
    return IntegerArray



def IterativeInsertion(IntegerArray, NumberElements):
    for Index in range(1, NumberElements):
        LastItem = IntegerArray[Index]
        CheckItem = Index

        while IntegerArray[CheckItem-1] > LastItem and CheckItem>0:
            IntegerArray[CheckItem], IntegerArray[CheckItem-1] = IntegerArray[CheckItem-1], IntegerArray[CheckItem]
            CheckItem -= 1
        
        IntegerArray[CheckItem] = LastItem
    
    return IntegerArray


print("iterative")
print(IterativeInsertion(NumberArray, len(NumberArray)))

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First >= Last:
        return -1
    
    Mid = (First+Last)//2

    if ToFind == IntegerArray[Mid]:
        return Mid
    elif ToFind > IntegerArray[Mid]:
        return BinarySearch(IntegerArray, Mid+1, Last, ToFind)
    elif ToFind < IntegerArray[Mid]:
        return BinarySearch(IntegerArray, First, Mid-1, ToFind)

res = BinarySearch(NumberArray, 0, len(NumberArray), 644)

if res == -1:
    print('Not found.')
else:
    print(f"Number was found at index {res}")