#defining the factorial function
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i;
    return fact
#accepting input for a number from user
num=int(input("Enter a number :"))
#printing the factorial
print('Factorial of',num,'is',fact(num))