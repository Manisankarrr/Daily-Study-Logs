#	167
def twoSum(nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -=1

nums = [2,7,11,15]
target = 9
ans  = twoSum(nums, target)
print(ans) # [1,2]
