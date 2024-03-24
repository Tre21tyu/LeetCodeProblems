class Solution:
    def isValid(self, s: str) -> bool:
        lf_rt_dict = { '(':')', '[':']', '{':'}'}
        tt_ct = { '(': 0, '[': 0, '{': 0, ')': 0, ']':0, '}': 0,}
        for i in range(len(s)):
            ct = 0
            if s[i] in tt_ct:
                tt_ct[s[i]] += 1
        if tt_ct['('] != tt_ct[')'] or tt_ct['['] != tt_ct[']'] or tt_ct['{'] != tt_ct['}']:
            return False
        for i in range(len(s)):
            if s[i] in lf_rt_dict
                if s[i + 1] != lf_rt_dict[s[i]]:
                    return False 
        return True
    # return tt_ct
soln = Solution()

test_1 = "()"
test_2 = "()[]{}"
test_3 = "(]"

print(soln.isValid(test_1))
print(soln.isValid(test_2))
print(soln.isValid(test_3))
