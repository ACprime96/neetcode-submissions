class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            n = len(s)
            res += "#" + str(len(str(n))) + str(n) + s

        return res

    def decode(self, s: str) -> List[str]:

        str_list = []
        i = 0
    
        while i < len(s):

            if s[i] == "#" and i < len(s) - 1:
                n_len = int(s[i+1]) 
                i += 2
                
                if i + n_len <= len(s):
                    s_len = s[i : i + n_len] 
                    start = i + n_len 
                    end = start + int(s_len) 
                    str_list.append(s[start:end])
                    i = end
            else:
                i += 1
        
        return str_list