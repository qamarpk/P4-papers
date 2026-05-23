class Node:
    def __init__(self, datap):
        self.NodeData = datap #Integer
        self.LeftNode = None #Node
        self.RightNode = None #Node

    def GetLeft(self):
        return self.LeftNode
    
    def GetRight(self):
        return self.RightNode
    
    def GetData(self):
        return self.NodeData

    def SetLeft(self, leftp):
        self.LeftNode = leftp

    def SetRight(self, rightp):
        self.RightNode = rightp
    
Node1 = Node(10) #Node
Node2 = Node(20)#Node
Node3 = Node(5)#Node
Node4 = Node(15)#Node
Node5 = Node(7)#Node

class Tree:
    def __init__(self, rootp):
        self.FirstNode = rootp #Node

    def GetRootNode(self):
        return self.FirstNode
    
    def Insert(self, NewNode):
        CurNode = self.GetRootNode()

        while CurNode != None:
            PrevNode = CurNode
            if NewNode.GetData() >= CurNode.GetData():
                CurNode = CurNode.GetRight()
                left = False
            else:
                CurNode = CurNode.GetLeft()
                left = True
        
        if left == True:
            PrevNode.SetLeft(NewNode)
        else:
            PrevNode.SetRight(NewNode)

def OutputInOrder(MyNode):
    if MyNode.GetLeft() != None:
        OutputInOrder(MyNode.GetLeft())
    
    print(MyNode.GetData())

    if MyNode.GetRight() != None:
        OutputInOrder(MyNode.GetRight())

MyTree = Tree(Node1)
MyTree.Insert(Node2)
MyTree.Insert(Node3)
MyTree.Insert(Node4)
MyTree.Insert(Node5)

OutputInOrder(Node1)