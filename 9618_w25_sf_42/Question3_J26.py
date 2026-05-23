global TreeArray, RootPointer, FreeNode

TreeArray = [[-1,-1,-1] for x in range(50)] #TreeArray as 2d array (50x3) of type integer
RootPointer = -1    #RootPointer as Integer
FreeNode = 0        #FreeNode as Integer

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

try:
    myfile = open("TreeData.txt", 'r')

    for line in myfile:
        AddNode(int(line.strip()))

    myfile.close()
except:
    print("File not found")

def WriteAllToFile():
    try:
        newfile = open("Tree.txt", 'w')

        for node in range(50):
            newfile.write(str(TreeArray[node][0])+","+str(TreeArray[node][1])+","+str(TreeArray[node][2])+"\n")
        
        newfile.close()
    
    except:
        print("Error: Not Adding to file")
    
WriteAllToFile()