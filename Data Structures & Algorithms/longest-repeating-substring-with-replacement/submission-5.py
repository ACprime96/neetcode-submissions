class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        letter_map = defaultdict(int)
        freq_c = 0
        l, r = -1, 0
        res = 0

        while r < len(s):
            if r - l - freq_c <= k:  
                letter_map[s[r]] += 1
                res = max(res, r-l)
                freq_c = max(letter_map.values())

                r += 1
                
            else:
                letter_map[s[l]] -= 1
                l += 1
                freq_c = max(letter_map.values())
        
        return res
