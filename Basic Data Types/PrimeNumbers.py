#defining the function
def prime(a,b):
    for i in range(a,b+1):
        c=2
        for j in range(2,i):
            if(i%j==0):
                c+=1
        if(c==2):
            print(i)

li=int(input("Enter lower interval :"))
ui=int(input("Enter lower interval :"))

#calling the function
prime(li,ui)
    