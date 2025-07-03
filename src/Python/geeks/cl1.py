def incdec(n, a, arr):
    if n == 0:
        return []
    first = sorted(arr[:a])
    second = sorted(arr[a:], reverse = True)
    return first + second

n = 8
a = 3
arr = [7, 9, 4, 3, 45, 76, 1, 2]

print(incdec(n, a, arr))  # Output should be sorted first part ascending and second part descending
#[4,7,9,76,45,3,2,1]