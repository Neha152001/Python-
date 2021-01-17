#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)

key=int(input("Enter the element to be searched :"))

#to find the element in the list 
for i in range(0,n):
    if l[i]==key:
        print(key,'is found at position',i+1)

print(key,'not found in the list')