stdata={'id':1,'name':'nirav','sub':'python'}
"""print(stdata)
print(stdata['name'])
print(stdata.get('sub'))

print(stdata.keys())
print(stdata.values())"""

print(stdata)
#stdata['id']=2
#print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

#print(len(stdata))
stdata['city']='Rajkot'
#stdata.pop('sub')
#stdata.clear()
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)
