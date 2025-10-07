class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last_used = s[0].lower()

        for c in s[1:]:
            if c.lower() != last_used.lower():
                changes += 1
                last_used = c
        
        return changes