def LongestSubstring(s):
    n = len(s)
    ans = set()
    l = 0
    longest = 0
    for r in range(n):
        while s[r] in ans:
            ans.remove(s[l])
            l+=1
        w = (r - l) + 1
        longest = max( longest, w)
        ans.add(s[r])
    return longest

s = "abcabcbb"
print(LongestSubstring(s))  # Output: 3