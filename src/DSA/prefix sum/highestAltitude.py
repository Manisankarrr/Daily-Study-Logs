#https://leetcode.com/problems/find-the-highest-altitude/

def largestAttitude(nums):
    n = 0
    c = 0
    for i in nums:
        c += i
        n = max(c,n)
    return n

nums = list(map(int, input("Enter num:").split()))
print(largestAttitude(nums))
