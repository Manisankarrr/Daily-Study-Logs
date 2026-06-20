n = int(input("Size: "))
arr = list(map(int,input("Elements: ").split()))
j = 0
count = -1
for i in arr:
    if i != 0:
        arr[j] = i
        j+=1
while j < n:
    arr[j] = 0
    j += 1
print(arr)


