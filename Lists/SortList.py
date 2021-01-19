#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)

#sort a list using in-bulit function
li=sorted(l)

for i in li:
    print(i,'\t',end="")