def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    if n == 0:
        return
    k = k % n

    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    arr[:] = reversed(arr)

    return arr

print(rotateArray([1, 2, 3, 4, 5, 6, 7], 3))
# Output: [4, 5, 6, 7, 1, 2, 3]
