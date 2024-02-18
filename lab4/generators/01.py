def sq(n):
    for i in range(1, n+1):
        yield i**2
n=int(input())

it=sq(n)
for i in range(1,n+1):
    print(next(it))