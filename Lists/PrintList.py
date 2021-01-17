#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=input("Enter the element :")
    l.append(z)

#printing the elements of the list 
for i in l:
    print(i,"\t",end="")