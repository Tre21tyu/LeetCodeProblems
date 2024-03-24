from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = sorted(set(nums))
        res = []
        for i in range(1, len(nums_s) - 1):
            if nums_s[i] - 1 == nums_s[i - 1]:
                res.append(nums_s[i]) 
            else:
                break
        # return len(res)
        # return [res, len(res)]
        return res
    # return len(nums)

soln = Solution()
# strange = [0,3,7,2,5,8,4,6,0,1]
print(soln.longestConsecutive([1,2,3,4, 100]))
# print(soln.longestConsecutive([100,4,199,1,3,2]))
# print(soln.longestConsecutive(strange))
