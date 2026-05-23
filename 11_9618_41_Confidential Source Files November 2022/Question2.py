class Card:
    #PRIVATE Number : INTEGER
    #PRIVATE Colour : STRING

    def __init__(self, nump, clrp):
        self.__number = nump
        self.__colour = clrp
    
    def GetNumber(self):
        return self.__number
    
    def GetColour(self):
        return self.__colour

RCard1 = Card(1, "red")
RCard2 = Card(2, "red")
RCard3 = Card(3, "red")
RCard4 = Card(4, "red")
RCard5 = Card(5, "red")
BCard1 = Card(1, "blue")
BCard2 = Card(2, "blue")
BCard3 = Card(3, "blue")
BCard4 = Card(4, "blue")
BCard5 = Card(5, "blue")
YCard1 = Card(1, "yellow")
YCard2 = Card(2, "yellow")
YCard3 = Card(3, "yellow")
YCard4 = Card(4, "yellow")
YCard5 = Card(5, "yellow")

class Hand:
    #PRIVATE Cards : ARRAY[0:9] OF Card
    #PRIVATE FirstCard : INTEGER
    #PRIVATE NumberCards : INTEGER

    def __init__(self, cardsp):
        self.__Cards = cardsp
        self.__FirstCard = cardsp[0]
        self.__NumberCards = len(cardsp)
    
    def GetCard(self, index):
        return self.__Cards[index]


Player1 = Hand([RCard1, RCard2, RCard3, RCard4, YCard1])
Player2 = Hand([YCard2, YCard3, YCard4, YCard5, BCard1])

def CalculateValue(myhand):
    plyrscr = 0

    for x in range(5):
        curcard = myhand.GetCard(x)

        if curcard.GetColour() == "red":
            plyrscr+=5
        elif curcard.GetColour() == "blue":
            plyrscr+=10
        elif curcard.GetColour() == "yellow":
            plyrscr+=15
        
        plyrscr+=curcard.GetNumber()
    
    return plyrscr

plyr1scr = CalculateValue(Player1)
plyr2scr = CalculateValue(Player2)

if plyr1scr > plyr2scr:
    print("Player 1 wins")
elif plyr1scr == plyr2scr:
    print("It is a draw")
else:
    print("Player 2 wins")