import math
s=int(input("Input number of sides: "))
l=float(input("Input the length of a side: "))
area=(s*l**2)/(4*math.tan(math.pi / s))
print("The area of the polygon is: ", area)