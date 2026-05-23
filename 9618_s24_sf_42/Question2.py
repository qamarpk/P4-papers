class Node():
    #DECLARE LeftPointer : INTEGER
    #DECLARE Data : INTEGER
    #DECLARE RightPointer : INTEGER

    def __init__(self, datap):
        self.LeftPointer = -1
        self.Data = datap
        self.RightPointer = -1

    def GetLeft(self):
        return self.LeftPointer   
     
    def GetRight(self):
        return self.RightPointer
    
    def GetData(self):
        return self.Data
    
    def SetLeft(self, newleft):
        self.LeftPointer = newleft

    def SetData(self, newdata):
        self.Data = newdata

    def SetRight(self, newright):
        self.RightPointer = newright

class TreeClass():
    #DECLARE Tree[0:19] : Node
    #DECLARE FirstNode : INTEGER
    #DECLARE NumberNodes : INTEGER

    def __init__(self):
        self.Tree = [Node(-1) for x in range(20)]
        self.FirstNode = -1
        self.NumberNodes = 0
    
    def InsertNode(self, NewNode):
        if self.FirstNode == -1:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            self.Tree[self.NumberNodes] = NewNode
            curpoint = self.FirstNode

            while curpoint != -1:
                prevpoint = curpoint
                if NewNode.GetData() > self.Tree[curpoint].GetData():
                    curpoint = self.Tree[curpoint].GetRight()
                    left = False
                elif NewNode.GetData() < self.Tree[curpoint].GetData():
                    curpoint = self.Tree[curpoint].GetLeft()
                    left = True

            if left:
                self.Tree[prevpoint].SetLeft(self.NumberNodes)
            else:
                self.Tree[prevpoint].SetRight(self.NumberNodes)

            self.NumberNodes+=1
    
    def OutputTree(self):
        if self.FirstNode == -1:
            print("No nodes.")
        else:
            for curnode in self.Tree:
                if curnode.GetData() != -1:
                    print(curnode.GetLeft(), "      ", curnode.GetData(), "       ",curnode.GetRight())

TheTree = TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))

TheTree.OutputTree()