def getSecondLargest(arr):
    if len(arr) < 2:
        return -1

    first = second = -1  # Initialize both to -1

    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i

    if second != -1:
        return second
    else:
        return -1

arr = list(map(int, input("Enter space-separated numbers: ").split()))
print("Second largest number:", getSecondLargest(arr))
