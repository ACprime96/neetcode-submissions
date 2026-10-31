class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        char_set = set()
        res = 0

        while r < len(s): 
            if s[r] not in char_set: 
                char_set.add(s[r])
                r += 1
                res = max(res , r-l)
            else:
                char_set.remove(s[l]) 
                l += 1
        
        return res
            

