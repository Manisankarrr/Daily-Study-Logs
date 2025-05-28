class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        
        max_avg = float(cur_sum) / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            avg = float(cur_sum) / k
            max_avg = max(max_avg, avg)
        
        return max_avg

# Example usage:
solution = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = solution.findMaxAverage(nums, k)
print(result)  # Output: 12.75