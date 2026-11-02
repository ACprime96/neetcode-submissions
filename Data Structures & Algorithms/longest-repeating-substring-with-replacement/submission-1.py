class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(lambda: 0)
        res = 0
        l = 0
        for ch in s:
            d[ch] += 1
            if len(d) > 1:
                mx, mn = max(d, key=d.get), min(d, key=d.get)
                res = max(res, sum(d.values())) if d[mn] <= k else res
                while d[mn] > k:
                    d[s[l]] -= 1
                    if not d[s[l]]:
                        d.pop(s[l])  
                    if d:
                        mx, mn = max(d, key=d.get), min(d, key=d.get)                  
                    l += 1
            else:
                res = max(res, sum(d.values()))

        return res