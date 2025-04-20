def sumRange(nums,left,right):
    n = 0
    p = [0]
    for i in nums:
        n += i
        p.append(n)
    return p[right + 1] - p[left]


nums = list(map(int, input("Enter array elements: ").split()))
left = int(input("Enter left index: "))
right = int(input("Enter right index: "))

print("Sum in range:", sumRange(nums, left, right))
