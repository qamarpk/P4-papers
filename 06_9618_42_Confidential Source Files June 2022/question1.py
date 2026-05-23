global StackData, StackPointer

StackData = [None for i in range(0,10)]
StackPointer = 0

def Output():
    global StackData, StackPointer

    for x in StackData:
        print(x)
    
    print("\n",StackPointer)

def Push(value):
    global StackData, StackPointer

    if StackPointer >= 10:
        return False
    else:
        StackData[StackPointer] = value
        StackPointer += 1
        return True
    
while True:
    userval = input("Enter a value: ")

    if Push(userval) == True:
        print("Number added")
    else:
        print("Number not added as stack is full")
        break

Output()

def Pop():
    global StackData, StackPointer

    if StackPointer == 0:
        return -1
    else:
        Returndata = StackData[StackPointer-1]
        StackData[StackPointer-1] = None
        StackPointer -= 1
        return Returndata

print("\n\n")
Pop()
Pop()

Output()