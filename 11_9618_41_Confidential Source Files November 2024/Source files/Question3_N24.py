global LinkedList #20 elements

LinkedList = [[-1,x+1] for x in range(20)]
LinkedList[19][1] = -1

FirstEmpty = 0

FirstNode = -1

def InsertData():
    global LinkedList, FirstEmpty, FirstNode

    for x in range(5):
        if FirstEmpty == -1:      #checking if list is full
            print("Linked list is full.")

        else:
            UserInt = int(input('Please enter your positive integer: '))        #input and validating it

            while UserInt <= 0:
                UserInt = int(input('Try again. Please enter a positive integer: '))

            LinkedList[FirstEmpty][0] = UserInt         #insert data

            if FirstNode == -1:                         #check if first element being added
                LinkedList[FirstEmpty][1] = -1
            else:                                       #if not changing pointer to taht pointed by first node
                LinkedList[FirstEmpty][1] = FirstNode

            FirstNode = FirstEmpty

            FirstEmpty = -1
            for x in range(20):                 #checking for the first empty element and making it -1 if list is full
                if LinkedList[x][0] == -1:
                    FirstEmpty = x
                    break

def OutputLinkedList():
    global LinkedList, FirstEmpty, FirstNode

    CurrentPoint = FirstNode
    while CurrentPoint != -1:           #LOOPS UNTIL it finds the end of the list
        print(LinkedList[CurrentPoint][0])
        CurrentPoint = LinkedList[CurrentPoint][1]

    
InsertData()
OutputLinkedList()



def RemoveData(DataToRemove):
    global LinkedList, FirstEmpty, FirstNode

    CurrentPointer = FirstNode

    if DataToRemove == LinkedList[CurrentPointer][0]:   #if first item in list is to be removed, we js move FirstNode Pointer
        LinkedList[CurrentPointer][0] = -1
        FirstNode = LinkedList[CurrentPointer][1]
    else:

        while  LinkedList[CurrentPointer][0] != DataToRemove:                         #looping to find the item to remove
            PrevPointer = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer][1]
        
        LinkedList[CurrentPointer][0] = -1                                          #remove the data

        LinkedList[PrevPointer][1] = LinkedList[CurrentPointer][1]                  #change pointer of previous node

    FirstEmpty = CurrentPointer                                                 #changing firstempty

RemoveData(5)
print("After")
OutputLinkedList()
