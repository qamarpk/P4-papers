class Horse():
    #PRIVATE Name : STRING
    #PRIVATE MaxFenceHeight : INTEGER
    #PRIVATE PercentageSuccess : INTEGER

    def __init__(self, namep, maxhp, prcsucessp):
        self.__Name = namep
        self.__MaxFenceHeight = maxhp
        self.__PercentageSuccess = prcsucessp
    
    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self, fenheight, fenrisk):
        resultprc = 0

        if fenheight > self.__MaxFenceHeight:
            resultprc = 0.2 * self.__PercentageSuccess
        else:
            if fenrisk == 5:
                resultprc = 0.6 * self.__PercentageSuccess
            elif fenrisk == 4:
                resultprc = 0.7 * self.__PercentageSuccess
            elif fenrisk == 3:
                resultprc = 0.8 * self.__PercentageSuccess
            elif fenrisk == 2:
                resultprc = 0.9 * self.__PercentageSuccess
            elif fenrisk == 1:
                resultprc = 1 * self.__PercentageSuccess
        
        return resultprc

    
#DECLARE Horses : ARRAY[0:1] OF Horse

Horses = [Horse("Beauty", 150, 72), Horse("Jet", 160, 65)]

for h in Horses: 
    print(h.GetName())


class Fence():
    #PRIVATE Height : INTEGER
    #PRIVATE Risk : INTEGER

    def __init__(self, hp, riskp):
        self.__Height = hp
        self.__Risk = riskp
    
    def GetHeight(self):
        return self.__Height
    
    def GetRisk(self):
        return self.__Risk

#DECLARE Course : ARRAY[0:3] OF Fence
Course = []

for x in range(4):
    userheight = int(input("Please enter fence height: "))

    while userheight < 70 or userheight > 180:          #validating height
        userheight = int(input("Invalid Fence Height. Please enter fence height again: "))

    userrisk = int(input("Please enter fence risk: "))
    
    while userrisk not in [1,2,3,4,5]:                  #validating risk
        userrisk = int(input("Invalid Fence Risk. Please enter fence risk again: "))
    
    Course.append(Fence(userheight, userrisk))

AveragePercentages = []

for horsey in Horses:
    totalprc = 0

    for fenceno in range(len(Course)):
        curprcsuccess = horsey.Success(Course[fenceno].GetHeight(), Course[fenceno].GetRisk())
        print(f"The horse {horsey.GetName()} at fence {fenceno+1} has a {curprcsuccess}% chance of success")
        totalprc += curprcsuccess
    
    avgprc = totalprc / len(Course)
    AveragePercentages.append(avgprc)
    print(f"The horse {horsey.GetName()} has an average {avgprc}% chance of jumping over all four fences")
    
print("The horse with greatest average is ", Horses[AveragePercentages.index(max(AveragePercentages))].GetName())

