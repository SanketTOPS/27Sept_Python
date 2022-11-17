mylist=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    el=input("Enter your list elements:")
    mylist.append(el)

#print(mylist)
mylist.reverse()

for i in mylist:
    print(i)




