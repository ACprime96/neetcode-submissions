class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "#" + str(len(s)) + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num_str = "0123456789" 
        k = 0
        while i < len(s):
            if i < len(s)-1 and  s[i] == "#" and s[i+1] in num_str:
                n = int(s[i+1])
                start = i+2
                end = i+2+n
                res.append(s[start:min(end, len(s))])
                i = end
        return res   