global Queue, Head, Tail

Queue = [-1 for x in range(100)]
Head = 0
Tail = 0

def Enqueue(itemadd):
    global Tail, Queue

    if Tail == 100:
        return False
    else:
        Queue[Tail] = itemadd
        Tail+=1
        return True

Added = True
for i in range(20):
    if Enqueue(i+1) == False:
        Added = False

print("Successful") if Added == True else print("Unsuccessful")

def RecursiveOutput(Start):
    global Head

    if Start == Head:
        return Queue[Head]
    else:
        return Queue[Start] + RecursiveOutput(Start-1)

print(RecursiveOutput(Tail-1))