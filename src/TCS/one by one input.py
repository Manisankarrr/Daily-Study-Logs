n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(arr)
for i in sorted(arr):
    print(i, end = " ")