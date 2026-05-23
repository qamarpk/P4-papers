class Card():
    #PRIVATE Number : INTEGER
    #PRIVATE Colour : STRRING

    def __init__(self, Numberp, Colourp):
        self.Number = Numberp
        self.Colour = Colourp

    def GetNumber(self):
        return self.Number
    
    def GetColour(self):
        return self.Colour
    
CardData = [] #Card

try:
    myfile = open("CardValues.txt", 'r')

    for x in range(30):
        num = myfile.readline()
        col = myfile.readline()

        CardData.append(Card(int(num), col))


    myfile.close
except IOError:
    print("File not found")

SelectedCards = []

def ChooseCard(index):
    while index<1 or index>30:
        index = int(input("please enter another index in range"))

    index-=1
    mycard = CardData[index]
    found = False

    if mycard in SelectedCards:
        index = 0
        while not found:
            if CardData[index] not in SelectedCards:
                found = True
                mycard = CardData[index]
            else:
                index += 1
            
    if found or mycard not in SelectedCards:
        SelectedCards.append(mycard)
        return index
    else:
        print("No empty card found")


Player1 = []
for cards in range(4):
    Player1.append(CardData[ChooseCard(int(input("Please choose an index for a card: ")))])
    print("Number: ", str(Player1[cards].GetNumber()))
    print("Colour: ", str(Player1[cards].GetColour()))

