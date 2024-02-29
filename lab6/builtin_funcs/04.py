import time
import math
def timee(num, t):
    time.sleep(t)
    return math.sqrt(num)
x=float(input("Enter num: "))
y=float(input("Enter time: "))
print(timee(x,y))