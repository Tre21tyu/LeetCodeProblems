class Solution:
    def isValid(self, s: str) -> bool:
        stk_mp_rvrs = { '(':')', '[':']', '{':'}'}
        stk_mp = { ')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c not in stk_mp:
                stack.append(c)
                continue
            if not stack or stack[-1] != stk_mp[c]:
                return False
            stack.pop()

        return not stack
soln = Solution()

test_1 = "()"
test_2 = "()[]{}"
test_3 = "(]"
test_4 = "([)]"


print(soln.isValid(test_1))
print(soln.isValid(test_2))
print(soln.isValid(test_2))
print(soln.isValid(test_3))
