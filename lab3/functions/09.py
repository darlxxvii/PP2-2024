"""Write a function that computes the volume
 of a sphere given its radius."""
import math
def vol(r):
    volume= 4/3 * (r**3)* math.pi
    return volume

rad=int(input("Enter radius of a sphere: "))
print(vol(rad))