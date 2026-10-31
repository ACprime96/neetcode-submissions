class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)

        if k > len(s2):
            return False
        s1_map = Counter(s1)
        s2_map = {}
        i = 0 
        while i + k <= len(s2): 
            if s1_map == Counter(s2[i:i+k]):
                return True
            i += 1
        
        return False
