fl=open('test.txt','a')

"""fl.write(id)
fl.write(name)
fl.write(sub)"""

id=input("Enter ID:")
name=input("Enter Name:")
sub=input("Enter Subject:")
fl.write(f"\nID:{id}\nName:{name}\nSubject:{sub}")

"""if fl.writable():
    print("Yes...")
else:
    print("Nooo....")"""