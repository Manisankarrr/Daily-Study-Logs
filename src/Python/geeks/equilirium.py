def equilibrium_point(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]

    return -1
# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 2, 2]
    result = equilibrium_point(arr)
    if result != -1:
        print(f"Equilibrium point is at index: {result}")
    else:
        print("No equilibrium point found.")