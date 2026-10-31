class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u = set()
        res = 0
        l = 0
        for i, ch in enumerate(s):
            if ch not in u:
                u.add(ch)
                res = max(len(u), res)
            else:
                while ch in u and l != i:
                    u.remove(s[l])
                    l += 1
                u.add(ch)                    
        return res

                    
        