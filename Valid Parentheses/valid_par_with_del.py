class Solution:
    def isValid(self, s: str) -> bool:
        lf_rt_dict = { '(':')', '[':']', '{':'}'}
        for i in range(len(s)):
            if len(s) > 0: 
                if s[i] in lf_rt_dict:
                    if lf_rt_dict[s[i]] in s:
                        idx = s.index(lf_rt_dict[s[i]])
                        s = s[:idx] + s[idx+0:]
                return False
        return True
soln = Solution()

test_1 = "()"
test_2 = "()[]{}"
test_3 = "(]"

print(soln.isValid(test_1))
print(soln.isValid(test_2))
print(soln.isValid(test_3))
