n=int(input())
def re(n):
    for i in range(n, -1, -1):
        yield i
it=re(n)
#print(*it)
for i in range(n+1):
    print(next(it))