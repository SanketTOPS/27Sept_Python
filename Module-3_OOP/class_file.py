import os

class client:

    clnm=""
    clct=""

    def location(self):
        if os.path.exists("Data"):
            print("This folder is already exists!")
        else:
            os.mkdir("Data")
            #os.chdir("Data")
        
    
    def getdata(self):
        fl=open("Data/clientdata.txt","a")
        self.clnm=input("Enter Name:")
        self.clct=input("Enter City:")
        fl.write(f"Name:{self.clnm}\n")
        fl.write(f"City:{self.clct}")

cl=client()
cl.location()
cl.getdata()




