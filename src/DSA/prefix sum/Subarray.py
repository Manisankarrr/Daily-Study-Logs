def subarr(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            print(nums[i:j+1])

nums = [1,2,3]
print(subarr(nums))