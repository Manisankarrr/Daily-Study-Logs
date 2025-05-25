def subb(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
                count += 1
    return count


nums = [1,2,3]
print(subb(nums))