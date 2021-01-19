#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)

#creating new list to copy 
li=list()

#copying the list
for i in l:
    li.append(i)

#printing the copied list 
for i in li:
    print(i,'\t',end="")