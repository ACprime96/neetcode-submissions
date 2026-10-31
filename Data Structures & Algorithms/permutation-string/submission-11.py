class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)

        if k > len(s2):
            return False

        s1_map = Counter(s1)
        s2_map = Counter(s2[0:k])
        if s1_map == s2_map:
            return True
        l = 0
        r = k


        while r < len(s2):
            s2_map[s2[l]] -= 1
            s2_map[s2[r]] += 1 

            if s1_map == s2_map:
                return True
            r += 1
            l += 1
        
        return False
