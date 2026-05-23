class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode
    

linkedList = [node(0,x+1) for x in range(0,10)] #10 elements of type node

startPointer = 0
emptyList = 5

linkedList[0].data = 1
linkedList[1].data, linkedList[1].nextNode = 5,4
linkedList[2].data, linkedList[2].nextNode = 6,7
linkedList[3].data, linkedList[3].nextNode = 7,-1
linkedList[4].data, linkedList[4].nextNode = 2,2
linkedList[6].nextNode = 8
linkedList[7].data, linkedList[7].nextNode = 56, 3
linkedList[9].nextNode = -1

def outputNodes(mylist, startpoint):
    curpoint = startpoint

    while curpoint != -1:
        print(linkedList[curpoint].data)
        curpoint = linkedList[curpoint].nextNode
    
outputNodes(linkedList, startPointer)

def addNode(mylist, start, empty):

    if empty == 0:
        return False
    else:
        itemadd = input("Enter value to add: ")

        heapPointer = 0
        while linkedList[heapPointer].data != 0:
            heapPointer +=1

        lastelement = start
        while linkedList[lastelement].nextNode != -1:
            lastelement = linkedList[lastelement].nextNode    

        linkedList[heapPointer].data = itemadd
        linkedList[lastelement].nextNode =  heapPointer
        linkedList[heapPointer].nextNode = -1

        return True


m21 = addNode(linkedList, startPointer, emptyList)
outputNodes(linkedList, startPointer)
