global Animals #ARRAY OF 10 STRING

Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

def SortDescending():
    global Animals

    ArrayLength = len(Animals)

    for X in range(0, ArrayLength-1):
        for Y in range(0, ArrayLength-X-1):
            if Animals[Y][0:1] < Animals[Y+1][0:1]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y+1]
                Animals[Y+1] = Temp

SortDescending()
for x in Animals: print(x)
