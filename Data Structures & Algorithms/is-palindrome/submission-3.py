class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c >= 'A' and c <= 'Z':
                res += chr(ord(c) + 32)

            elif ((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')):
                res += c
        print(res)
        l, r = 0, len(res)-1
        while l <= r : 
            if res[l] == res[r]:
                l += 1
                r -= 1
            else:
                return False
        return True 