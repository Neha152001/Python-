#importing math library
import math

#defining the function
def cubeSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=math.pow(i,3);
    return sum

#accepting the number 
n=int(input("Enter a number :"))
print('Cube Sum is',cubeSum(n))