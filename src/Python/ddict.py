from collections import defaultdict, Counter

s = "banana"
arr = defaultdict(list)
pos = Counter(s)

word = "qwiudqihfewu"
for i, c in enumerate(s):
    arr[c].append(i)

print("Character positions in 'banana':")
for char, indices in arr.items():
    print(f"{char}: {indices}")

print("\nCharacter counts in 'banana':")
for i, c in pos.items():
    print(f"{i}: {c}")

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for char in s + t:
            res ^= ord(char)
        return chr(res)

# Example usage of Solution
sol = Solution()
s1 = "abcd"
t1 = "abcdefghjkl"
print(f"\nThe extra character in '{t1}' compared to '{s1}' is: '{sol.findTheDifference(s1, t1)}'")

print(f"\nWord: {word}")