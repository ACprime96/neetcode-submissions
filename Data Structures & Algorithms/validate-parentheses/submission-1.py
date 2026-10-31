class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if stk and stk[-1] == '(' and ch == ')':
                stk.pop()
            elif stk and stk[-1] == '{' and ch == '}':
                stk.pop()
            elif stk and stk[-1] == '[' and ch == ']':
                stk.pop()
            else:
                stk.append(ch)
        return True if not stk else False