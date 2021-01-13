import math

#defining armstrong number function
def armstrong(n):
    save=n
    num=0
    while(n>0):
        r=n%10
        num+=int(math.pow(r,3))
        n=int(n/10)
    if(save==num):
        print(save,'is a Armstrong Number')
    else:
        print(save,'is not a Armstrong number')

#taking input of a number
n=int(input("Enter a number :"))

#calling the function
armstrong(n)

