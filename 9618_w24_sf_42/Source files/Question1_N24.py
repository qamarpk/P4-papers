class EventItem():
    #PRIVATE EventName : String
    #PRIVATE Type : String
    #PRIVATE Difficulty : Integer

    def __init__(self, namep, typep, diffp):
        self.__EventName = namep
        self.__Type = typep
        self.__Difficulty = diffp
    
    #getters:

    def GetName(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetEventType(self):
        return self.__Type

Group = [] #5 elements of type EventItem

Group = [EventItem("Bridge", "jump", 3), EventItem("Water wade", "swim", 4), EventItem("100 mile run", "run", 5), EventItem("Gridlock", "drive", 2), EventItem("Wall on wall", "jump", 4)]

class Character():
    #PRIVATE CharacterName : String
    #PRIVATE Jump : Integer
    #PRIVATE Swim : Integer
    #PRIVATE Run : Integer 
    #PRIVATE Drive : Integer

    def __init__(self, namep, jumpp, swimp, runp, drivep):     
        self.__CharacterName = namep
        self.__Jump = jumpp
        self.__Swim = swimp
        self.__Run = runp
        self.__Drive = drivep

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, Type, Difficulty):
        #finding type of the character
        if Type == "jump": 
            skilllevel = self.__Jump
        elif Type == "swim": 
            skilllevel = self.__Swim
        elif Type == "run": 
            skilllevel = self.__Run
        elif Type == "drive": 
            skilllevel = self.__Drive
        
        #calculating the percentage
        if skilllevel >= Difficulty:
            return 100
        else:
            difference = Difficulty - skilllevel

            if difference == 1:
                return 80
            elif difference == 2:
                return 60
            elif difference == 3:
                return 40
            elif difference == 4:
                return 20

#DECLARE Tarz, Geni : Character

Tarz = Character("Taz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

TarzPoints = 0
GeniPoints = 0

for EvInd in range(5):
    #finding percentage for each event
    TarzPrc = Tarz.CalculateScore(Group[EvInd].GetEventType(), Group[EvInd].GetDifficulty())
    GeniPrc = Geni.CalculateScore(Group[EvInd].GetEventType(), Group[EvInd].GetDifficulty())

    #comparing percentages
    if TarzPrc > GeniPrc:
        print(f"Tarz has won event: \"{Group[EvInd].GetName()}\"")
        TarzPoints+=1
    elif TarzPrc < GeniPrc:
        print(f"Geni has won event: \"{Group[EvInd].GetName()}\"")
        GeniPoints+=1
    else:
        print(f"The event \"{Group[EvInd].GetName()}\" was a draw")

#final results
if TarzPoints > GeniPoints:
    print("Tarz has the most points in the group.")
elif TarzPoints < GeniPoints:
    print("Geni has the most points in the group.")
else:
    print("The group was a draw")