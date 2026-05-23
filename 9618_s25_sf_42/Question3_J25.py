class Animal:

    def __init__(self, namep, soundp, sizep, intep):
        self.Name = namep   #String
        self.Sound = soundp #String
        self.Size = sizep #Integer
        self.Intelligence = intep   #Integer
    
    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence is {self.Intelligence}."

class Parrot(Animal):

    def __init__(self, namep, soundp, sizep, intep, wingsp, nwp):
        super().__init__(namep, soundp, sizep, intep)
        self.WingSpan = wingsp #Integer
        self.NumberWords = nwp #Integer
    
    def ChangeNumberWords(self, addedw):
        self.NumberWords += addedw
    
    def Description(self):
        return super().Description() + f" It has a wingspan of {self.WingSpan} and can say {self.NumberWords} words."


class Wolf(Animal):

    def __init__(self, namep, soundp, sizep, intep, tsizep):
        super().__init__(namep, soundp, sizep, intep)
        self.TerritorySize = tsizep #Integer
    
    def SetTerritorySize(self, addedts):
        self.TerritorySize += addedts

    def Description(self):
        return super().Description() + f" Its territory is {self.TerritorySize} square miles."

Chewie = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
Nighteyes = Wolf("Nigheyes", "Howl", 8, 7, 100)
Copper = Animal("Copper", "Neigh", 10, 6)

Nighteyes.SetTerritorySize(-20)
Chewie.ChangeNumberWords(2)
print(Chewie.Description())
print(Nighteyes.Description())
print(Copper.Description())