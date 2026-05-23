class Queue():
    def __init__(self, arrayp, headpp, tailpp):
        self.QueueArray = arrayp    #100 elements of Integer
        self.Headpointer = headpp   #integer
        self.Tailpointer = tailpp   #integer

TheQueue = Queue([-1 for x in range(100)], -1, 0)

def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer += 1
        return 1
    else:
        if AQueue.Tailpointer > 99:
            return -1
        else:
            AQueue.QueueArray[AQueue.Tailpointer] = TheData
            AQueue.Tailpointer += 1
            return 1

def ReturnAllData():
    global TheQueue

    returnstr = ""
    for index in range(TheQueue.Headpointer, TheQueue.Tailpointer):     #concatenate
        returnstr = returnstr + str(TheQueue.QueueArray[index]) + " "
    
    return returnstr

for no in range(10):
    userint = int(input("Enter your integer: "))
    while userint < 0:
        userint = int(input("Integer must be greater than or equal to 0. Enter your integer: "))
    
    if Enqueue(TheQueue, userint) == -1:
        print("Integer not added, Queue is full.")
    else:
        print("Integer added successfully")

print(ReturnAllData())

def Dequeue():
    global TheQueue

    if TheQueue.Headpointer == -1 or TheQueue.Headpointer == TheQueue.Tailpointer:
        return -1
    else:
        result = TheQueue.QueueArray[TheQueue.Headpointer]

        TheQueue.Headpointer += 1

        return result
    
res1 = Dequeue()
res2 = Dequeue()

if res1 == -1:
    print("Queue empty")
else:
    print(res1)

    if res2 == -1:
        print("Queue empty")
    else:
        print(res2)

print(ReturnAllData())
