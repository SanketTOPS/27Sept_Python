class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

# Calling via Object
"""st=student()
st.getdata()
st.stid=23
st.stnm='Nirav'
st.getdata()"""

# Calling via Instance
student().getdata()
student().stid=34
student().stnm='Ashok'
student().getdata()