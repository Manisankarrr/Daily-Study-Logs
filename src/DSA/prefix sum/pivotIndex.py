def pivot(nums):
    total = sum(nums)
    lsum = 0
    for i in range(len(nums)):
        rsum = total - nums[i] - lsum
        if(lsum == rsum):
            return i
        lsum += nums[i]
    return -1


nums = list(map(int, input("Enter num: ").split()))
print(pivot(nums))