def pivot(nums):
    total = sum(nums)
    lsum = 0
    for i, num in enumerate(nums):
        if lsum == (total - lsum - i):
            return i
        lsum += num
    return -1

    

nums = [1, 7, 3, 6, 5, 6]
print(pivot(nums))