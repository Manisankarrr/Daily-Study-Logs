def hello(nums,k):
    res = []
    for i in range(0,len(nums),k):
        a = nums[i:i+k]
        b = "".join(map(str,a))
        res.append(b)
    return res


k = 2
arr = [1,0,2,3,4,5]
a = hello(arr,k)
print(a)