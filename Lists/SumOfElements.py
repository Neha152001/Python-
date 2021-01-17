#creating the empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number of elements :"))

sum=0

#accepting the input
for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)
    sum+=z

print('Sum of all the elements of the list is',sum)