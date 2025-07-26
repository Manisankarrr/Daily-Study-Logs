from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            hash_map[sorted_s].append(s)

        return list(hash_map.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
