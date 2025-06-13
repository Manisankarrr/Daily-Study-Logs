def find_duplicates(arr):
    dup = set()
    seen = set()

    for i in arr:
        if i in seen:
            dup.add(i)
        else:
            seen.add(i)
    
    return list(dup)  # Fixed missing parenthesis

arr = list(map(int, input("Enter space-separated numbers: ").split()))
