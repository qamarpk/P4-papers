import datetime


class Character():
    def __init__(self, pname, pDOB, pint, pspeed):
        self.CharacterName = pname      #STRING
        self.DateOfBirth = pDOB         #DATE
        self.Intelligence = pint        #REAL
        self.Speed = pspeed             #INTEGER

    def GetIntelligence(self):
        return self.Intelligence
    
    def GetName(self):
        return self.CharacterName

    def SetIntelligence(self, newint):
        self.Intelligence = newint

    def Learn(self):
        self.SetIntelligence(self.Intelligence * 1.1)
    
    def ReturnAge(self):
        return 2023 - self.DateOfBirth.year

FirstCharacter = Character("Royal", datetime.date(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
print(f"The character {FirstCharacter.GetName()} has an age of {FirstCharacter.ReturnAge()} and an intelligence of {FirstCharacter.GetIntelligence()}")

class MagicCharacter(Character):
    def __init__(self, pname, pDOB, pint, pspeed, pelement):
        super().__init__(pname, pDOB, pint, pspeed)
        self.Element = pelement             #STRING
    
    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
            self.SetIntelligence(self.Intelligence * 1.2)
        elif self.Element == "earth":
            self.SetIntelligence(self.Intelligence * 1.3)
        else:
            self.SetIntelligence(self.Intelligence * 1.1)
        
FirstMagic = MagicCharacter("Light", datetime.date(2018, 3, 3), 75, 22, "fire")
FirstMagic.Learn()
print(f"The character {FirstMagic.GetName()} has an age of {FirstMagic.ReturnAge()} and an intelligence of {FirstMagic.GetIntelligence()}")