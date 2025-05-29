def missing_num(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    actual = sum(arr)
    return total - actual  # Directly return the missing value

arr = list(map(int, input("Enter space-separated numbers: ").split()))

print("Missing number:", missing_num(arr))
