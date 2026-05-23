class Bird:
    def __init__(self, speciesp, dph):
        self.__DistancePerHour = dph    #DistancePerHour as Real
        self.__Species = speciesp       #Species as String
        self.__XPosition = 500.0         #XCoordinate as Real
        self.__YPosition = 500.0         #YCoordinate as Real

    def GetSpecies(self):
        return self.__Species

    def GetPosition(self):
        return "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)
    
    def Move(self, direction, minutes):
        if direction == 'N':
            self.__YPosition += ((self.__DistancePerHour/60)*minutes)
        elif direction == 'S':
            self.__YPosition -= ((self.__DistancePerHour/60)*minutes)
        elif direction == 'E':
            self.__XPosition += ((self.__DistancePerHour/60)*minutes)
        elif direction == 'W':
            self.__XPosition -= ((self.__DistancePerHour/60)*minutes)

Cockatiel = Bird("Cockatiel", 71.0)   #Cockatiel as object of Bird
Macaw = Bird("Macaw", 56.0)           #Macaw as object of Bird


print("Species: " + Cockatiel.GetSpecies() + " " + Cockatiel.GetPosition())
print("Species: " + Macaw.GetSpecies() + " " + Macaw.GetPosition())


userspecies = input("Enter species: ")
while userspecies != "Cockatiel" and userspecies != "Macaw":
    userspecies = input("Invalid. Enter species again: ")

userdir = input("Enter direction traveled (N,S,E,W): ")
while userdir != "N" and userdir != "S" and userdir != "E" and userdir != "W":
    userdir = input("Invalid. Enter direction (N,S,E,W) again: ")

userminutes = round(float(input("Enter time traveled (nearest minute): ")))
while userminutes < 0 :
    userminutes = input("Invalid. Enter time traveled (nearest minute): ")  

if userspecies == "Cockatiel":
    Cockatiel.Move(userdir,float(userminutes))
    print("Species: " + Cockatiel.GetSpecies() +" "+ Cockatiel.GetPosition())
elif userspecies == "Macaw":
    Macaw.Move(userdir,float(userminutes))
    print("Species: " + Macaw.GetSpecies() +" "+ Macaw.GetPosition())