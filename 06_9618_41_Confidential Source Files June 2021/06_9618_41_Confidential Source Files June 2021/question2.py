global arrayData

arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearSearch(value):
    found = False
    index = 0
    while found == False and index<10:
        if arrayData[index] == value:
            found = True
        else:
            index+=1
    
    return found

userint = int(input("Enter a value: "))
found = linearSearch(userint)
if found: print("The value was found")
else: print("The value was not found")

def bubbleSort():
    for x in range(0,10):
        for y in range(0,9):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

bubbleSort()
print(arrayData)