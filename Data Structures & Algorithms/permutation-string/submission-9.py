class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)

        if k > len(s2):
            return False
        s1_map = Counter(s1)
        s2_map = {}
        for i in range(len(s2)):
            if i + k <= len(s2): 
                print(i, k, Counter(s2[i:i+k]))
                if s1_map == Counter(s2[i:i+k]):
                    return True
        
        return False
