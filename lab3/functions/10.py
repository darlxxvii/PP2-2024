"""Write a Python function that takes a list and returns a new list with unique elements
 of the first list. Note: don't use collection set."""
def func(nums):
    new=[]
    c=True
    for i in range(x):
        for j in range(x):
            if int(nums[i])==int(nums[j]) and i!=j:
                c=False
        if c==True:
            new.append(nums[i])
        c=True
    return new
nums=input("Enter list: ").split()
x=len(nums)
print(func(nums))