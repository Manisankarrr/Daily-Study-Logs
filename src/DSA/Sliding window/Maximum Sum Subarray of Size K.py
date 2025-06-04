def maxSumSubarray(nums, k):
    n = len(nums)
    if n < k:
        return 0  
    cur = 0
    for i in range(k):
        cur += nums[i]
    
    max_sum = cur

    for i in range(k, n):
        cur += nums[i]
        cur -= nums[i - k]
        max_sum = max(max_sum,cur)
    return max_sum
# Example usage:

nums = [2, 1, 5, 1, 3, 2]
k = 3
result = maxSumSubarray(nums, k)
print(result)