def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    if n == 0:
        return
    k = k % n

    arr[n - k:] = reversed(arr[n-k:])
    arr[:n-k] = reversed(arr[:n-k])
    arr[:] = reversed(arr)

    return arr

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original array:", arr)
    rotated_arr = rotateArray(arr, k)
    print("Rotated array:", rotated_arr)