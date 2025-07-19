def jg(nums):
    n = len(nums)
    jumps = 0
    far = 0
    end = 0
    for i in range(n-1):
        far = max(far, i+nums[i])
        if i == end:
            jumps += 1
            end = far

    return jumps

nums = list(map(int,input().split()))
print(jg(nums))