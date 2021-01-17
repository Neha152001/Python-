#creating a empty list
l=list()

#accepting the number of elements
n=int(input("Enter the number  of elements :"))

for i in range(1,n+1):
    z=int(input("Enter the element :"))
    l.append(z)

for i in l:
    if i%2==0:
        print("Even number :",i)
    else:
        print('Odd number :',i)