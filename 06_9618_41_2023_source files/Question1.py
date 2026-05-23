global DataArray # 25 INT
DataArray = []

try:
    myfile = open("Data.txt")

    for n in range(25):
        DataArray.append(int(myfile.readline().strip()))

    myfile.close()
except IOError:
    print("File not found")

def PrintArray(myarray):
    for item in myarray:
        print(item, end=" ")

PrintArray(DataArray)
print()

def LinearSearch(myarray, intsearch):
    count = 0

    for x in myarray:
        if x == intsearch:
            count+=1
    
    return count

userint = int(input("Please enter integer: "))

while userint<0 or userint>100:
    userint = int(input("Invalid. Please enter integer: "))

print(f"The number {userint} is found {LinearSearch(DataArray, userint)} times.")