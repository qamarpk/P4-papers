import random

global Stack, TopOfStack

Stack = [-999 for x in range(30)] #30 integers
TopOfStack = -1 #Integer

def Push(IntAdd):
    global TopOfStack, Stack

    if TopOfStack == 29:    #checking for full
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = IntAdd
        return True
    
def Pop():
    global TopOfStack, Stack

    if TopOfStack == -1:    #checking for empty
        return -999
    else:
        IntReturn = Stack[TopOfStack]
        Stack[TopOfStack] = -999
        TopOfStack -= 1
        return IntReturn

for ints in range(40):
    if Push(random.randint(0, 1000)) == False:
        print("Stack full")
        break

def FindValues():
    MaxValue = 0
    MinValue = 10000

    for x in range(30):
        CurInt = Pop()
        if CurInt > MaxValue:
            MaxValue = CurInt
        if CurInt < MinValue:
            MinValue = CurInt

    print(f"The largest number in stack was {MaxValue}")
    print(f"The smallest number in stack was {MinValue}")

FindValues()