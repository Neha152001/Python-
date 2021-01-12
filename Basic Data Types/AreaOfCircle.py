#importing math library
import math

#defining area function
def area(r):
    return (math.pi*r*r)

#accepting the value of radius
rad=float(input("Enter radius of the circle :"))
print('Area of circle with radius',rad,'is',area(rad))