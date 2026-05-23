def ReadData():
    try:
        myfile = open("Data.txt", 'r')

        myarray = myfile.readlines()  #making array of lines

        for x in range(len(myarray)):   #removing \n from each element
            myarray[x] = myarray[x].strip()

        myfile.close()

        return myarray

    except IOError:
        print("File not found")

def FormatArray(arrayp):
    result = ""

    for x in arrayp:    #concatenating string
        result = result + x + " "
    
    return result

DataArray = ReadData()
print(FormatArray(DataArray))

def CompareStrings(str1, str2):
    charno = 0

    while True:
        if str1[charno] > str2[charno]:     #comparing string slices
            return 2
        elif str1[charno] < str2[charno]:
            return 1
        else:
            charno += 1

def Bubble(myarray):
    swap = True
    top = len(myarray) - 1

    while swap and top > 0:     #1st loop
        swap = False

        for x in range(top):        #2nd loop
            if CompareStrings(myarray[x], myarray[x+1]) == 1:
                myarray[x], myarray[x+1] = myarray[x+1], myarray[x]
                swap = True
        
        top = top-1

    return myarray

SortedArray = Bubble(DataArray)
print(FormatArray(SortedArray))

