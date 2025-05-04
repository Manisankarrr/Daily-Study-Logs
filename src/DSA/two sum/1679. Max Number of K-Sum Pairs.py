def maxOperations(nums, k):
        left, right = 0, len(nums)-1
        count = 0
        while(left < right):
            s = nums[left] + nums[right]
            if s == k:
                left += 1
                right -=1
                count += 1
            elif s < k:
                left+=1
            else:
                right-=1
        return count
nums = [1,2,3,4]
k = 5
ans = maxOperations(nums, k)
print(ans) # 2