Queue = [-1 for x in range(20)] #20 integers

HeadPointer = -1 #integer
TailPointer = -1 #integer
NumberItems = 0 #integer

def Enqueue(DataAdd):
    global Queue, HeadPointer, TailPointer, NumberItems

    if NumberItems == 20:   #chcek for full
        return False
    else:
        if HeadPointer == -1:   #check for start
            HeadPointer = 0
        
        TailPointer += 1

        if TailPointer == 20:   #making queue circular
            TailPointer = 0

        Queue[TailPointer] = DataAdd

        NumberItems+=1
        return True

for Int in range(1, 26):
    if Enqueue(Int) == True:        #checking if successfull
        print(Int, " Successful")
    else:
        print(Int, " Unsuccessful")

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems

    if NumberItems == 0:        #checking for empty
        return -1
    else:
        returnint = Queue[HeadPointer]

        Queue[HeadPointer] = -1

        HeadPointer+=1

        if HeadPointer == 20:       #making queue circular
            HeadPointer = 0

        NumberItems-=1
        return returnint


print("removed ", Dequeue())
print("removed ", Dequeue())