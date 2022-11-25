class grandfather:
    gold=0
    house=0

    def getdata(self):
        self.gold=input("Enter gold details:")
        self.house=input("Enter house detail:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def printdata(self):
        print("Gold:",self.gold)
        print("House:",self.house)
        print("Car:",self.car)
        print("Balance:",self.bal)

sn=son()
sn.getdata()
sn.f_getdata()
sn.printdata()