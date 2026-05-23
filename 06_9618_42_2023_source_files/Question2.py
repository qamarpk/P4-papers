class SaleData:
    def __init__(self, id, quantity):
        self.SaleID = id
        self.SaleQuantity = quantity

CircularQueue = [SaleData("", -1) for x in range(5)]

Head = 0
Tail = 0
NumberofItems = 0

def Enqueue(newrec):
    global NumberofItems, Tail, CircularQueue

    if NumberofItems == 5:
        return -1
    else:
        CircularQueue[Tail] = newrec
        Tail+=1
        if Tail==5: Tail=0

        NumberofItems+=1
        return 1
    


def Dequeue():
    global NumberofItems, Head, CircularQueue

    if NumberofItems == 0:
        return SaleData("", -1)
    else:
        outp = CircularQueue[Head]
        Head+=1
        if Head==5: Head=0

        NumberofItems-=1

        return outp

def EnterRecord():
    myid = input("Please enter Sale ID: ")
    myquantity = int(input("Please enter Sale Quantity: "))

    myrecord = SaleData(myid, myquantity)

    if Enqueue(myrecord) == -1:
        print("Full")
    else:
        print("Stored")

for x in range(6): EnterRecord()

remrec = Dequeue()

if remrec.SaleID == "" and remrec.SaleQuantity==-1:
    print("The queue is empty")
else:
    print(f"The sale ID is {remrec.SaleID} and quantity is {remrec.SaleQuantity}")

EnterRecord()

for x in CircularQueue:
    print(f"The sale id is {x.SaleID} and quantity is {x.SaleQuantity}")

