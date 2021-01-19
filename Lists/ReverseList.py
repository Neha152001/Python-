#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)

#printing before reverse 
print('List Before :')
for i in l:
    print(i,"\t",end="")

print('\n')

#using in-bulit function reverse 
li=reversed(l)

print('List After :')
for i in li:
    print(i,"\t",end="")


