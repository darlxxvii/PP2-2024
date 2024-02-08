"""Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""
import math
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        return self.x, self.y
    def move(self):
        a=int(input("Enter a for x: "))
        b=int(input("Enter b for y: "))
        self.x=self.x+a
        self.y=self.y+b
        return self.x, self.y
    def dist(self):
        p1=int(input("Enter p1:"))
        p2=int(input("Enter p2:"))
        distance=math.sqrt((self.x-p1)**2 + (self.y-p2))
        return distance
x=int(input("Enter coordinate x: "))
y=int(input("Enter coordinate y: "))
point1=Point(x,y)
print(point1.show())
print(point1.move())
print(point1.dist())