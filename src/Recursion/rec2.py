def multiple(n):
    if n == 1:
        return n
    else:
        return multiple(n-1) * n
    
print(multiple(5))  # Output: 120
