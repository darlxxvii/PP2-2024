n=int(input())
def func(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
it=func(n)
print(*it)