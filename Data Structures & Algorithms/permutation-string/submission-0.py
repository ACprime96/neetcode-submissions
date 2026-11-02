class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_map = Counter(s1)
        s2_map = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            if s2[r] not in s1_map:
                continue
            else:

                while s2[r] in s1_map:
                    s2_map[s2[r]] += 1
                    r += 1
                if s1_map == s2_map:
                    return True
                else:
                    s2_map[s2[l]] -= 1
                    l += 1
        
        return False

        
