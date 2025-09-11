def min_number_after_removal(num_str):
    n = len(num_str)
    min_val = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            val = num_str[i] + num_str[j]
            min_val = min(min_val, int(val))
    return min_val



num = input("Enter a number: ")  
print("Minimum number after removing 2 digits:", min_number_after_removal(num))
