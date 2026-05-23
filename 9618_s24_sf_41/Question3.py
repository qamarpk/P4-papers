global QueueHead, QueueTail #INTEGER
global QueueData #20 STRING

QueueData = [None for x in range(20)]
QueueHead = -1
QueueTail = -1

def Enqueue(Itemadd):
    global QueueData, QueueHead, QueueTail

    if QueueTail == 19:
        return False
    else:
        if QueueHead == -1: QueueHead = 0

        QueueTail +=1
        QueueData[QueueTail] = Itemadd
        return True

def Dequeue():
    global QueueData, QueueHead, QueueTail

    if QueueHead == -1 or QueueTail < QueueHead:
        return "false"
    else:
        returnitem = QueueData[QueueHead]
        QueueData[QueueHead] = None
        QueueHead += 1
        return returnitem

def StoreItems():
    global QueueData, QueueHead, QueueTail

    invalidcount = 0

    for x in range(10):

        userinp = input("Enter value to add: ")
        mycheckdig = (int(userinp[0]) + int(userinp[1])*3 + int(userinp[2]) + int(userinp[3])*3 + int(userinp[4]) + int(userinp[5])*3)//10

        if str(mycheckdig) == userinp[6] or (mycheckdig == 10 and userinp[6] == "X"):
            if Enqueue(userinp[0:6]) == True:
                print("The number has been entered.")
            else:
                print("The Queue is full.")
        else:
            invalidcount+=1
    
    print(invalidcount, " values were invalid.")

StoreItems()
outp = Dequeue()
if outp == "false":
    print("The queue was empty.")
else:
    print(outp)
        
