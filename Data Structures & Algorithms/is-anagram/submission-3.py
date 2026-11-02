class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return counter(t) == counter(s)