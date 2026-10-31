class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            num_len = len(str(n))
            res += "#" + str(num_len) + str(n) + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num_str = "0123456789" 
        k = 0
        while i < len(s):
            if s[i] == "#" and i+1 < len(s):
                n_len = int(s[i+1])
                n = int(s[i+2: i+2+n_len])
                start = i + 2 + n_len
                end = start + n
                res.append(s[start: end])
                i = end

        return res   