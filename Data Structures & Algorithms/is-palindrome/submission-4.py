class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t=""
        for c in s:
            if ord(c) >= ord('A') and ord(c) <= ord('Z') :
                t += chr(ord(c)+32)
            elif (ord(c) >= ord('a') and ord(c) <= ord('z')) or c in "0123456789":
                t += c
        
        l, r = 0, len(t)-1
        while l<=r:
            
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1

        return True
