# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]


def is_palindrome(s):
    left, right = 0, len(s) - 1
    s = s.lower()
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True




s = "MaDAm"
a = is_palindrome(s)
print(a)

