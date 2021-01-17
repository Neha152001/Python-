#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)

min=l[0]
max=l[0]

#to find the largest and smallest element in the list
for i in l:
    if(i>max):
        max=i
    if(i<min):
        min=i

print('Largest element is',max,end="")
print(' Smallest element is',min)
