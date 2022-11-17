myset={'A','B','C','D','E','F','A','B'}


#print(len(myset))

"""if 'B' in myset:
    print("Yes..")
else:
    print("Noo..")"""

# -------------------------- #

print(myset)

"""for i in myset:
    print(i)"""

#myset.add('G')
#myset.update(['H','I','J'])
#myset.remove('B')
#myset.pop()
#print(myset)

newset={'P','Q','R','S','A','B'}
#x=myset.union(newset)
x=myset.intersection(newset)
print(x)