#defining a function to calculate compound intrest
def ci(p,r,t):
    principal=p
    for i in range(1,t+1):
        amt=p+(p*r*1)/100;
        p=amt 
    print('Principal Amount is',principal)
    print('Rate of intrest is',r,"%")
    print('Time is',t,'years')
    print('Compound Intrest is',(amt-principal))
    print('Total Amount is',amt)

#taking input for principal,ratoe of intrest and time
p=float(input("Enter the principal amount :"))
r=float(input("Enter the rate of intrest :"))
t=int(input("Enter the time :"))

#calling the compound intrest function
ci(p,r,t)
