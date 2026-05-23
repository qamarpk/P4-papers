class Employee():
    #PRIVATE HourlyPay : REAL
    #PRIVATE EmployeeNumber : STRING
    #PRIVATE JobTitle : STRING
    #PRIVATE PayYear2022 : ARRAY[0:51] OF REAL

    def __init__(self, hpay, enum, jtitle):
        self.__HourlyPay = hpay
        self.__EmployeeNumber = enum
        self.__JobTitle = jtitle
        self.__PayYear2022 = [0 for x in range(52)]
    
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, weekno, noofhours):
        self.__PayYear2022[weekno-1] = self.__HourlyPay*noofhours
    
    def GetTotalPay(self):
        Total = 0
        for x in self.__PayYear2022: Total+=x

        return Total

class Manager(Employee):
    #PRIVATE BonusValue : REAL 

    def __init__(self, bvalue, hpay, enum, jtitle):
        self.__BonusValue = bvalue
        super().__init__(hpay, enum, jtitle)
        
    def SetPay(self, weekno, noofhours):
        return super().SetPay(weekno, noofhours*(1 + (self.__BonusValue/100)))

EmployeeArray = [None for x in range(8)]

try:
    datafile = open("Employees.txt")
    for curemployee in range(8):
        curhpay = float(datafile.readline())
        curenum = datafile.readline()
        line3 = datafile.readline()

        try:
            line3 = float(line3)
            curjtitle = datafile.readline()

            EmployeeArray[curemployee] = Manager(line3, curhpay, curenum, curjtitle)

        except:
            EmployeeArray[curemployee] = Employee(curhpay, curenum, line3)


    datafile.close()    
except FileNotFoundError:
    print("Cannot find file")




def EnterHours():
    hoursfile = open("HoursWeek1.txt")

    for Emp in range(8):
        tempnum = hoursfile.readline()
        temphworked = float(hoursfile.readline())

        for z in EmployeeArray:
            if z.GetEmployeeNumber() == tempnum:
                z.SetPay(1, temphworked)
                break
    
    hoursfile.close()

EnterHours()
for e in EmployeeArray:
    print(e.GetEmployeeNumber(), end="")
    print(e.GetTotalPay())
    print()
