class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            n = len(s)
            res += "#" + len(str(n)) + str(n) + s

        return res

    def decode(self, s: str) -> List[str]:

        str_list = []

        while i < len(s):
            if s[i] == "#" and i < len(s) - 1:
                n_len = int(s[i+1])
                i += 1
                if i + n_len < len(s):
                    s_len = s[i : i + n_len]
                    start = i + n_len
                    end = start + int(s_len)
                    str_list.append(s[start:end])
        
        return str_list