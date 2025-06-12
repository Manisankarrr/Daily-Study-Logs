def countpairs(nums, target):
    seen = set()
    pairs = set()
    for num1 in nums:
        num2 = target - num1
        if num2 in seen:
            pairs.add(tuple(sorted((num1,num2))))
        seen.add(num1)
    return len(pairs), pairs



nums = [1, 5, 7, -1, 5]
target = 6
ans = countpairs(nums, target)
print("Number of pairs:", ans[0])
print("Pairs:", ans[1])