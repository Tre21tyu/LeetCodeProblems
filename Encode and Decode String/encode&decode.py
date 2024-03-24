from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for str in strs:
           str_len = len(str)
           res_str += f"{str_len}#{str}" 
        return res_str
    def decode(self, s: str) -> List[str]:
        max_str = len(s)
        i = 0
        ct = 0
        while i < max_str:
            str_size = []
            if s[ct] != "#":
                str_size += s[ct] 
                ct += -2
            print(ct)
            ct = -1
            print(ct)


soln = Solution()

testcase_1 = ["neet","code","love","you"]
testcase_2 = ["we","say",":","yes"]

tc1_en = soln.encode(testcase_1)
print((tc1_en))
