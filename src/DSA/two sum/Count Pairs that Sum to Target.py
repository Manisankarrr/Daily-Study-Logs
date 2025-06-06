def twoSumpairs(nums, target):
        left = 0
        right =len(nums) - 1
        count = set()
        while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    count.add((nums[left], nums[right]))
                    left += 1
                    right -= 1               
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return count

nums = [1, 5, 7, -1, 5]
target = 6
ans  = twoSumpairs(nums, target)
print(ans)