def has_33(nums):
    for i in range(0,x-1):
        if int(nums[i])==3 and int(nums[i+1]) == 3:
            return True
    return False

nums=input("Enter numbers: ").split()
x=len(nums)
print(has_33(nums))