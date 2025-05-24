def summ(nums):
    result =[]
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        result.append(total)
    return result

nums = [1, 2, 3, 4]
print(summ(nums))