fl=open('test.txt','r+')

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[1])

fl.write("\nHello Students!")

"""for i in fl:
    print(i)"""

"""if fl.readable():
    print("Yes...")
else:
    print("Noo")    """
fl.close()