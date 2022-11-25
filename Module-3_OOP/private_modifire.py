class student:
    stid=0
    stnm=""

    def __getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")
    
    def printdata(self):
        self.__getdata()
        print("Student ID:",self.stid)
        print("Student ID:",self.stnm)


st=student()
st.printdata()
