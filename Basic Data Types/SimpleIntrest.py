#function to calaculate simple intrest
def si(p,r,t):
    si=(p*r*t)/100
    amt=p+si
    print('Principal Amount is',p)
    print('Rate of intrest is',r,"%")
    print('Time is',t,'years')
    print('Simple Intrest is',si)
    print('Total Payable Amount is',amt)

#taking input for principal,ratoe of intrest and time
p=float(input("Enter the principal amount :"))
r=float(input("Enter the rate of intrest :"))
t=float(input("Enter the time :"))

#calling the si function
si(p,r,t)