class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        def dist_to_a(c):
            return (ord('z') - ord(c) + 1) % 26

        def right_shift(c, times):
            val = ord(c) - ord('a')
            val += times
            val %= 26
            return chr(ord('a') + val)

        def get_rep(s):
            shifts = dist_to_a(s[0])
            return tuple([right_shift(x, shifts) for x in s])
        
        for s in strings:
            rep = get_rep(s)
            res[rep].append(s)
    
        return list(res.values())
