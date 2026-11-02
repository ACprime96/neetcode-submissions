class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)

        if k > len(s2):
            return False
        s1_map = Counter(s1)
        s2_map = {}
        for i in range(1, len(s2)-k):
            print(Counter(s2[i:i+k]))
            if s1_map == Counter(s2[i:i+k]):
                return True
        
        return False
