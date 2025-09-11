# def find_indices_to_remove(s, to_remove):
#     indices = []
#     remove_index = 0
#     for i, ch in enumerate(s):
#         if remove_index < len(to_remove) and ch == to_remove[remove_index]:
#             indices.append(i)
#             remove_index += 1
#     return indices

# # Example usage
# s = "raceyuicar"
# to_remove = "yui"

# indices = find_indices_to_remove(s, to_remove)
# print("Original String:", s)
# print("Characters to remove:", to_remove)
# print("Indices to remove:", indices)


def palindrome(s):
    clean  = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

# Example usage of palindrome function
s = "Was it a car or a cat I saw?"
print(f"Is the string '{s}' a palindrome? {palindrome(s)}")
