class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        l = 0
        res = 0
        for r, ch in enumerate(s):
            counts[ord(ch) - 65] += 1
            maxf = max(counts)
            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                counts[ord(s[l]) - 65] -= 1
                l += 1
        return res