def twosum(nums, target):
    map = {}
    for i, num1 in enumerate(nums):
        num2 = target - num1
        if num2 in map:
            return [map[num2], i]
        map[num1] = i
    return []

nums = [2, 1, 5, 3]
target = 3

print(twosum(nums, target))