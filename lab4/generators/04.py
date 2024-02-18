a=int(input())
b=int(input())
def sq(a,b):
    for i in range(a,b+1):
        yield i**2

it=sq(a,b)
print(*it)