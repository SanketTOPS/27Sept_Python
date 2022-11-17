techlist=['Python','Php','JAVA','NET']

"""print(techlist)
print(techlist[0])
print(techlist[-1])
print(techlist[0:3])
print(techlist[2:])
print(techlist[:3])"""

#print(len(techlist))

#print(techlist)

"""for i in techlist:
    print(i)"""

"""n=0
for i in techlist:
    print(f"Index[{n}] = {i}")
    n+=1"""

#print(techlist.index('JAVA'))

"""for i in techlist:
    print("Index[{techlist.index(i)}] = {i}")
"""
# Index[0] = Python
# Index[1] = Php

"""if 'JAVA' in techlist:
    print("Yes...")
else:
    print("No..")"""

# -------------------------------------------#

#print(techlist)
techlist.append('Node')
techlist.insert(2,'React')
#techlist.pop()
#techlist.pop(2)
#techlist.remove('Python')
#del techlist[2]
#del techlist
#techlist.clear()
#print(techlist)

#newlist=techlist.copy()
#print(newlist)
#techlist.sort()
#techlist.reverse()
print(techlist)

newlist=["C","C++","DS","C#"]
#print(newlist+techlist)
newlist.extend(techlist)
print(newlist)