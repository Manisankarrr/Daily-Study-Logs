def twosum(nums, target):
    map = {}
    for i, num1 in enumerate(nums):
        num2 = target - num1
        if num2 in map:
            return [map[num2], i]
        map[num1] = i
    return []

nums = [3, 2, 4]
target = 6

print(twosum(nums, target))