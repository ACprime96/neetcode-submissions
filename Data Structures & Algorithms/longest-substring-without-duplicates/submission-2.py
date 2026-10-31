class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        maxLen = 0
        charSet = set()
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r+=1
            else:
                while l < len(s) and s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                
            maxLen = max(maxLen, r-l)

        return maxLen    
