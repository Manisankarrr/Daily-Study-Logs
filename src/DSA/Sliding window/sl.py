def maxlen(arr, k):
    n = len(s)
    max_length = 0
    start = 0
    count = 0
    sum = 0
    for end in range(n):
        sum += arr[start]
        while(sum >= k and start <= end):
            sum -= arr[start]
            start += 1
        count = end - start + 1
        max_length = max(max_length, count)
    return max_length

# Example usage:
s = [1, 2, 3, 4, 5]
k = 5
result = maxlen(s, k)
print(result)  