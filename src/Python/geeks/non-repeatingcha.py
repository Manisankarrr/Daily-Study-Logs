class Solution:
    def nonRepeatingChar(self,s):
        #code here
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch,0) + 1
        for ch in mp:
            if mp[ch] == 1:
                return ch
        return -1