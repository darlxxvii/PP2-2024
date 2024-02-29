#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
from operator import mul
def mul_list(num):
    return reduce(mul, num, 1)
list=[]
for i in range(5):
    c=int(input())
    list.append(c)
print(list)

mul_li=[1,2,3,4,5]
print(mul_list(list))

