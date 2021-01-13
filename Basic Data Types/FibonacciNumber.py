#defining the function
def fib(n):
    if n<=1:
        return n
    elif n==0:
        return 0
    elif n==1:
        return 1
    
    return fib(n-1)+fib(n-2)

n=int(input("Enter the number :"))
print(n,'fibonacci number is ',fib(n))