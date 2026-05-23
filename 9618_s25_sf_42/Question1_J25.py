global Stack, TopOfStack
Stack = ["-1" for x in range(20)] #String 20 elements
TopOfStack = -1 #Integer

def Push(DataAdd):
    global Stack, TopOfStack
    if TopOfStack >= 19:    #checking for full
        return -1
    else:
        TopOfStack+=1
        Stack[TopOfStack] = DataAdd
        return 1

def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:        #checking for empty
        return "-1"
    else:
        DataRemove = Stack[TopOfStack]
        Stack[TopOfStack] = -1
        TopOfStack-=1
        return DataRemove
    
def ReadData(FileName):
    try:
        myFile = open(FileName, 'r')

        for line in myFile:                     #reading lines
            if Push(line.strip()) == -1:        
                print("Stack Full")

        myFile.close()
    except:
        print("File Not Found.")

def Calculate():

    Finished = False
    Total = int(Pop())

    while not Finished:
        operation = Pop()
        number = int(Pop())

        if operation == '+':        #checking operation
            Total = Total + number
        elif operation == '-':
            Total = Total - number
        elif operation == '/':
            Total = Total / number
        elif operation == '*':
            Total = Total * number
        elif operation == '^':
            Total = Total**number
        elif operation == "-1":
            Finished = True
        
    return Total
        
fname = input("Please Enter File Name: ")
ReadData(fname)
print(f"Total is {Calculate()}")

