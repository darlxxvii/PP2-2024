def prime(num):
    if num<=1:
        return False
    for j in range(2,int(num**0.5)+1):
        if num%j==0:
            return False
    return True
def filter_prime():
    primes=[]
    for i in numbers:
        if i.isdigit() and prime(int(i)):
            primes.append(i)
    return primes

numbers=input("Enter numbers with spaces: ").split()

print("Prime numbers list: ", filter_prime())
