class student:
    __stid=12
    __stnm="Sanket"

    def __getdata(self):
        #print("This is getdata.")
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)
    
    def printdata(self):
        self.__getdata()


st=student()
#st.getdata()
st.printdata()