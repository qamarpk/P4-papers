class Train():
    #DECLARE TrainIDNumber : STRING
    #DECLARE Route : INTEGER
    def __init__(self, IDp, Routep):
        self.__TrainIDNumber = IDp  
        self.__Route = Routep

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber
    
    def GetRoute(self):
        return self.__Route
    
Train1 = Train("12ADV", 134)#Train
Train2 = Train("33ART", 20) #Train
Train3 = Train("9FKF", 3)   #Train
Train4 = Train("21VBC", 24) #Train

class Station():
    #DECLARE StationID : STRING
    #DECLARE NumberPlatforms : INTEGER
    #DECLARE Trains[0:9] : Train
    #DECLARE NumberTrains : INTEGER
    def __init__(self, sIDp, NoPlatformp):
        self.__StationID = sIDp
        self.__NumberPlatforms = NoPlatformp
        self.__Trains = []
        self.__NumberTrains = 0

    def AddTrain(self, NewTrain):
        if self.__NumberPlatforms == self.__NumberTrains:
            return False
        else:
            self.__Trains.append(NewTrain)
            self.__NumberTrains += 1
            return True
    
    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains"
        else:
            FinalString = f"The trains at station {self.__StationID} are :\n"
            for trn in self.__Trains:
                FinalString += f"{trn.GetTrainIDNumber()} on route number {trn.GetRoute()}\n"
            return FinalString
    
Station1 = Station("STH", 2)
Station2 = Station("NTH", 1)

if Station1.AddTrain(Train1) == False:
    print("Station is full")

if Station1.AddTrain(Train2) == False:
    print("Station is full")

if Station1.AddTrain(Train3) == False:
    print("Station is full")

if Station2.AddTrain(Train4) == False:
    print("Station is full")

print(Station1.GetTrains())
print(Station2.GetTrains())