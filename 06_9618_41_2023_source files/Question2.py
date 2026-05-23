class Vehicle():
    #PRIVATE ID : STRING
    #PRIVATE MaxSpeed : INTEGER
    #PRIVATE CurrentSpeed : INTEGER
    #PRIVATE IncreaseAmount : INTEGER
    #PRIVATE HorizontalPosition : INTEGER

    def __init__(self, idp, maxspdp, incramntp):
        self.__ID = idp
        self.__MaxSpeed = maxspdp
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = incramntp
        self.__HorizontalPosition = 0
    
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, newspd):
        self.__CurrentSpeed = newspd

    def SetHorizontalPostion(self, newhzp):
        self.__HorizontalPosition = newhzp
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount

        if self.__CurrentSpeed > self.__MaxSpeed: 
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed

class Helicopter(Vehicle):
    #PRIVATE VerticalPosition : INTEGER
    #PRIVATE VerticalChange : INTEGER
    #PRIVATE MaxHeight : INTEGER

    def __init__(self, idp, maxspdp, incramntp,  vtchp, maxhghtp):
        super().__init__(idp, maxspdp, incramntp)
        self.__VerticalPosition = 0
        self.__VerticalChange = vtchp
        self.__MaxHeight = maxhghtp
    
    def GetVerticalPosition(self):
        return self.__VerticalPosition
    
    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange

        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        return super().IncreaseSpeed()

def Output(myveh):
    print("The horizontal position is ", myveh.GetHorizontalPosition())
    print("The current speed is ", myveh.GetCurrentSpeed())

    if type(myveh) == Helicopter:
        print("The Vertical position is ", myveh.GetVerticalPosition())
    

Car = Vehicle("Tiger", 100, 20)
HeliLion = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()


Output(Car)

HeliLion.IncreaseSpeed()
HeliLion.IncreaseSpeed()

Output(HeliLion)