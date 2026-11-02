class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = set(s1)
        s1_map = Counter(s1)
        s2_map = defaultdict(int)
        l = r = 0

        while r < len(s2):
            if s2[r] not in s1_map:
                r+=1
                continue
            else:
                l = r
                while r < len(s2) and s2[r] in s1_map:
                    s2_map[s2[r]] += 1
                    if s1_map == s2_map:
                        return True
                    r += 1
                print(s2_map)
                s2_map[s2[l]] -= 1
                l += 1
                print(l, s2_map)
        
        return s1_map == s2_map

        
