fl=open('test.txt','a')

id=input("Enter ID:")
name=input("Enter Name:")
sub=input("Enter Subject:")

"""fl.write(id)
fl.write(name)
fl.write(sub)"""

fl.write(f"\nID:{id}\nName:{name}\nSubject:{sub}")