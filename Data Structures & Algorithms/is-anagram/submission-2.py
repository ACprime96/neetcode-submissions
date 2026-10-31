class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_map = Counter(s)
        t_char_map = Counter(t)

        return s_char_map == t_char_map