class Solution:    
    def findUnion(self, a, b):
        arr = []
        seen = set()
        for num in a+b:
            if num not in seen:
                seen.add(num)
        return seen