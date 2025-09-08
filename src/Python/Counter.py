from collections import Counter

m = [1,2,3,3,4,5,3,2,1,3,4,2,1,2,3,3,3,1]
freq = Counter(m)
print(freq[5])

arr = [1, 2, 3, 2, 4]
arr = [x for x in arr if x != 2]
j = 0
for x in arr:
    if x!= 2:
        arr[j] = x
        j += 1
print(arr)