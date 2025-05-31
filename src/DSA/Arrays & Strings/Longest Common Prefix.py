class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = float('inf')
        i = 0

        for s in strs:
            min_len = min(min_len, len(s))

        
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1        
        return s[:i]
# Example usage:
strs = ["flower", "flow", "flight"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)  # Output: "fl"
