class Solution:
    def isPalindrome(self, s: str) -> bool:
        chs = [ch.lower() for ch in s if ch.isalnum()]
        n = len(chs)
        mid = n // 2
        l, r = (mid - 1, mid) if n % 2 == 0 else (mid, mid)
        while l >= 0 and r < n:
            if chs[l] != chs[r]:
                return False
            l -= 1
            r += 1
        return True