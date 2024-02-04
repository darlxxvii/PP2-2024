"""Write a program to solve a classic puzzle: We count 35 heads and 
94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens
 do we have? create function: solve(numheads, numlegs):"""
a=32 #numheads
b=94 #numlegs
def solve(a,b):
        for x in range(a+1):
            r=a-x
            if 2*x + 4*r == b:
                  return x, r
print("Chickens and Rabbits: ", solve(a,b))


    
