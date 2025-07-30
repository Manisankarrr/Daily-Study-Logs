def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    result = []

    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    i = j = 0
    
    while(i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    while(i < len(left)):
        result.append(left[i])
        i += 1
    while(j < len(right)):
        result.append(right[j])
        j += 1
    # result.extend(left[i:])
    # result.extend(right[j:])
    return result

arr = list(map(int,input().split(':')))
sorted_arr = merge_sort(arr)
print("Sorted array (Merge Sort):", sorted_arr)
