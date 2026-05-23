#1. Linear Search
print("Linear Search:")


mylist = [34,23,12,21,42,61,1,32,12,129]

item = int(input("Enter value to be found: "))
found = False
index = -1

for x in range(0, len(mylist)):
    if item == mylist[x]:
        found = True
        index = x
        break
    
if found: print("Item was found at " + str(index)) 
else: print("Not found")

#2. Binary Search:
print("\n\n\n\nBinary Search:")

mylist.sort()
found = False
up = len(mylist)-1
low = 0
item = int(input("Enter value to be found: "))

while (not found) and (low<=up):
    mid = (up+low)//2
    if item == mylist[mid]:
        found = True
        index = mid
    elif item > mylist[mid]:
        low = mid + 1
    elif item < mylist[mid]:
        up = mid - 1

if found: print("Item was found at " + str(index)) 
else: print("Not found")

#3. Bubble sort
print("\n\n\n\nBubble sort:")


mylist = [34,23,12,21,42,61,1,32,12,129]
top = len(mylist)
swap = True

while swap and top>0:
    swap = False
    for index in range(top-1):
        if mylist[index] > mylist[index+1]:
            temp = mylist[index]
            mylist[index] = mylist[index+1]
            mylist[index+1] = temp
            swap = True
        
    top-=1

print(mylist)

#4. Insertion sort
print("\n\n\n\nInsertion sort:")

mylist = [34,23,12,21,42,61,1,32,12,129]

for index in range(1,len(mylist)):
    item = mylist[index]
    counter = index
    while counter>0 and mylist[counter-1] > item:
        mylist[counter] = mylist[counter-1]
        counter = counter-1
    
    mylist[counter] = item

print(mylist)

#5. Stack operarions
print("\n\n\n\nStack:")

mystack = [None for index in range(0,10)]
basepointer = 0
toppointer = -1
stackfull = 10

def pop():
    global toppointer
    if toppointer == basepointer-1:
        print("stack is empty")
    else:
        toppointer-=1
        return mystack[toppointer+1]
        

def push(value):
    global toppointer, mystack
    if toppointer<stackfull-1:
        toppointer+=1
        mystack[toppointer] = value
        
    else:
        print("Stack is full")

    
push(123)
push(2112)
push(721)
print(pop())
push(72121)
print(mystack)

#6. Queue
print("\n\n\n\nQueue:")

myqueue = [None for index in range(0,10)]
backpointer = 0
frontpointer = -1
queueitems = 0

def enqueue(value):
    global myqueue, frontpointer, queueitems
    if queueitems>10:
        print("Queue is full")
    else:
        queueitems+=1
        frontpointer+=1
        if frontpointer>=10:
            frontpointer=0
        myqueue[frontpointer] = value

def dequeue():
    global myqueue, backpointer, queueitems
    if queueitems == 0:
        print("queue is empty")
    else:
        queueitems-=1
        value = myqueue[backpointer]
        myqueue[backpointer] = None
        backpointer+=1
        if backpointer>=10:
            backpointer = 0
        return value

enqueue(212)
enqueue(12782)
enqueue(2912)
print(dequeue())
dequeue()

print(myqueue)

#7. Linked list
print("\n\n\n\nLinked List:")


heapStartPointer = 0
StartPointer = -1

myLinkedList = [ None for y in range(0,12)]
myLinkedListPointers = [ x+1 for x in range(0,12)]


myLinkedListPointers[11] = -1

def Find(itemfind):
    global StartPointer, heapStartPointer, myLinkedList, myLinkedListPointers
    if StartPointer == -1:
        print("linked list is empty.")
    else:
        found = False
        curpointer = StartPointer
        while not found and curpointer!=-1:
            if myLinkedList[curpointer] == itemfind:
                found = True
            else:
                curpointer = myLinkedListPointers[curpointer]
        
        print("found") if found else print("not found")        

def Add(itemadd):
    global heapStartPointer, StartPointer, myLinkedList, myLinkedListPointers
    if heapStartPointer == -1:
        print('Linked list is full.')
    else:
        tempPointer = StartPointer
        StartPointer = heapStartPointer
        heapStartPointer = myLinkedListPointers[heapStartPointer]
        myLinkedList[StartPointer] = itemadd
        myLinkedListPointers[StartPointer] = tempPointer

def Delete(itemremove):
    global heapStartPointer, StartPointer, myLinkedList, myLinkedListPointers
    if StartPointer == -1:
        print("linked list is empty")
    else:
        curindex = StartPointer
        oldindex = None
        while curindex!=-1 and myLinkedList[curindex]!=itemremove:
            oldindex = curindex
            curindex = myLinkedListPointers[curindex]
        
        if curindex == -1:
            print(f"item {itemremove} not found")
        else:
            
            temppointer = myLinkedListPointers[curindex]

            if curindex == StartPointer:
                StartPointer = temppointer
            else:
                myLinkedListPointers[oldindex] = temppointer

            myLinkedList[curindex] = None
            myLinkedListPointers[curindex] = heapStartPointer
            heapStartPointer = curindex




Add(2)
Add(82)
Add(2781)
Add(1221)
Find(211)
Delete(2)
print(str(myLinkedList))
print(myLinkedListPointers)
print(f"startpointer: {StartPointer}")
print(f"heapstartpointer: {heapStartPointer}")

#9. Binary Tree without class (might not work)
print("\n\n\n\nBinary Tree (without class):")

global TreeArray, RootPointer, FreeNode

TreeArray = [[-1,-1,-1] for x in range(50)] #[LeftPointer, Data, RightPointer]
RootPointer = -1    
FreeNode = 0        

def Findtree(itemsearch):
    nowpointer = RootPointer
    while nowpointer != -1:
        if TreeArray[nowpointer][1] > itemsearch:
            nowpointer = TreeArray[nowpointer][0]
        elif TreeArray[nowpointer][1] < itemsearch:
            nowpointer = TreeArray[nowpointer][2]
        else:
            return nowpointer

def AddNode(dataadd):
    global TreeArray, RootPointer, FreeNode
    if FreeNode == 50:
        print("Tree is full")
    elif RootPointer == -1:
        RootPointer += 1
        TreeArray[FreeNode][1] = dataadd
    else:
        TreeArray[FreeNode][1] = dataadd
        CurPointer = RootPointer
        Found = False
        while not Found:
            if dataadd < TreeArray[CurPointer][1]:
                if TreeArray[CurPointer][0] == -1:
                    TreeArray[CurPointer][0] = FreeNode
                    Found = True
                else:
                    CurPointer = TreeArray[CurPointer][0]
            else:
                if TreeArray[CurPointer][2] == -1:
                    TreeArray[CurPointer][2] = FreeNode
                    Found = True
                else:
                    CurPointer = TreeArray[CurPointer][2]
    
    FreeNode += 1
        
AddNode(2)
AddNode(12)
AddNode(13)
print(Findtree(13))



#10. Binary tree with OOP and recursion:
print("\n\n\n\nBinary Tree (with OOP and recursion):")

class node():
    def __init__(self, itemp):
        self.item = itemp
        self.left = -1
        self.right = -1


    def insert(self, additem):
        if self.item!=additem:
            if additem < self.item:
                if self.left == -1:
                    self.left = node(additem)
                else:
                    self.left.insert(additem)
            elif additem > self.item:
                if self.right == -1:
                    self.right = node(additem)
                else:
                    self.right.insert(additem)

    
    def search(self, item):
        while self.item != item:
            if item < self.item:
                if self.left == -1:
                    return -1
                item = self.left.search(item)
                break
            elif item > self.item:
                if self.right == -1:
                    return -1
                item = self.right.search(item)
                break
        return item
    
    def display(self):
        if self.left:
            self.left.display()
        print(self.item, end=" ")
        if self.right:
            self.right.display()
    


tree = node(27)
tree.insert(32)
tree.insert(12)
tree.insert(2)
print("Found") if tree.search(12) != -1 else print("Not found")
