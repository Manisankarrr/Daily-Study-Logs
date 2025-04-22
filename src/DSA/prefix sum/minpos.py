# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

def minStartValue(nums):
    total = 0
    min_sum = 0

    for num in nums:
        total += num
        min_sum = min(min_sum, total)

    # We want the minimum prefix sum to be at least 1
    return -min_sum + 1

# Example usage:
nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))  # Output: 5
