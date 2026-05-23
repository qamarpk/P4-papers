global Jobs #ARRAY[0:99, 0:1] OF INTEGER
global NumberOfJobs #INTEGER

Jobs = []

def Initialize():
    global Jobs, NumberOfJobs

    Jobs = [[-1 for x in range(2)] for y in range(100)]
    NumberOfJobs = 0


def AddJob(Jobno, priority):
    global Jobs, NumberOfJobs

    if NumberOfJobs >= 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = Jobno
        Jobs[NumberOfJobs][1] = priority


        NumberOfJobs+=1
        print("Added")

Initialize()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


def InsertionSort():
    global Jobs

    for index in range(1,100):
        key = Jobs[index][1]
        place = index-1

        if Jobs[place][1] > key:
            while Jobs[place][1] > key and place>=0:
                Jobs[place][1], Jobs[place+1][1] = Jobs[place+1][1], Jobs[place][1]
                Jobs[place][0], Jobs[place+1][0] = Jobs[place+1][0], Jobs[place][0]
                place-=1
            Jobs[place+1][1] = key


def PrintArray():
    for x in Jobs:
        if x[1] != -1:
            print(f"{x[0]} priority {x[1]}")

InsertionSort()
PrintArray()