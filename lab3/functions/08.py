def spy_game(nums):
    for i in range(x-2):
        if int(nums[i])==0:
            for j in range(i+1, x-1):
                if int(nums[j])==0:
                    for k in range(j+1, x):
                        if int(nums[k])==7:
                            return True
    return False
nums=input("Enter numbers: ").split()
x=len(nums)
print(spy_game(nums))