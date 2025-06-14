def find_leaders(arr):
    leader = []
    rmax = arr[-1]  # Last element is always a leader
    leader.append(rmax)

    for i in range(len(arr)-2, -1, -1):  # Iterate from second-last to first
        if arr[i] >= rmax:
            rmax = arr[i]
            leader.append(rmax)

    return leader[::-1]  # Reverse to maintain original order

arr = [16, 17, 4, 3, 5, 2]  
print("Leaders in the array:", find_leaders(arr))
