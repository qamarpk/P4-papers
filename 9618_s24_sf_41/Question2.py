class Tree():
    #PRIVATE TreeName : STRING
    #PRIVATE HeightGrowth : INTEGER
    #PRIVATE MaxHeight : INTEGER
    #PRIVATE MaxWidth : INTEGER
    #PRIVATE Evergreen : STRING

    def __init__(self, namep, growthp, maxhp, maxwp, evergreenp):
        self.__TreeName = namep
        self.__HeightGrowth = growthp
        self.__MaxHeight = maxhp
        self.__MaxWidth = maxwp
        self.__Evergreen = evergreenp
    
    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth
    
    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen


def ReadData():
    TreeData = []

    try:
        treefile = open("Trees.txt", 'r')

        
        curtree = ["a"]
        while curtree[0] != "":
            curtree = treefile.readline().strip().split(",")

            if curtree[0] != "":
                TreeData.append(Tree(curtree[0], int(curtree[1]), int(curtree[2]), int(curtree[3]), curtree[4]))

        treefile.close()
    except IOError:
        print("File not found.")
    
    return TreeData

def PrintTrees(myTree):
    if myTree.GetEvergreen() == "Yes":
        print(f"{myTree.GetTreeName()} has a maximum height {myTree.GetMaxHeight()} a maximum width {myTree.GetMaxWidth()} and grows {myTree.GetGrowth()} cm a year. It does not lose its leaves.")
    else:
        print(f"{myTree.GetTreeName()} has a maximum height {myTree.GetMaxHeight()} a maximum width {myTree.GetMaxWidth()} and grows {myTree.GetGrowth()} cm a year. It lose its leaves each year.")
    

TreeData = ReadData()
PrintTrees(TreeData[0])

def ChooseTree(TreeArray):
    NewTreeArray = []

    usermaxh = int(input("Enter maximum height required: "))
    usermaxw = int(input("Enter maximum width required: "))
    userevg = input("Enter whether tree should be evergreen: ")

    for curtr in TreeArray:
        if curtr.GetMaxHeight() <= usermaxh and curtr.GetMaxWidth() <= usermaxw and curtr.GetEvergreen() == userevg:
            NewTreeArray.append(curtr)
    
    if NewTreeArray == []:
        print("No trees meet the requirements.")
    else:
        for tr in NewTreeArray: PrintTrees(tr)
    
    TreeToBuy = input("Enter name of tree to buy: ")
    HeightWhenBought = int(input("Enter height at time of purchase: "))
    
    for t in NewTreeArray:
        if t.GetTreeName() == TreeToBuy:
            print("Your tree should reach max height in ", ((t.GetMaxHeight() - HeightWhenBought) / t.GetGrowth()), "years.")
        
ChooseTree(TreeData)