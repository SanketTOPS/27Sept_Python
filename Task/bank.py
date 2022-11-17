#ch='Y'

nm=input("Enter Name:")
atype=input("Enter account type:")
dep=int(input("Enter deposite amount:"))
ch=input("Plz enter your choice for withdraw:")

def deposite():
   if dep>1000:
    print("Error! Plz deposite minimum 1000" )

def withdrwan():
    if am<dep:
        # Print all the data
        print("Fullname:",nm)
        print("A/c Type:",atype)
        print("Total Balance:",dep)
        rem=dep-am
        print("Remaining Balance:",rem)
    else:
        print("Error!")

if ch=='Y' or ch=='y':
    am=int(input("Enter an amount:"))
    deposite()
    withdrwan()
else:
    print("Thank you...Visit again!")


