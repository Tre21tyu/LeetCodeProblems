from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst_set = set(nums)
        set_len = len(lst_set)
        ans = 0
        for i in range(len(nums)):
            if (nums[i] - 1) in lst_set:
                continue  # Skip this iteration and continue with the next one
            j = 0
            while j != set_len:
                if (nums[i] + j + 1) in lst_set:
                    j += 1
                else:
                    break
            if (j + 1 > ans):
                ans = j + 1

        return ans

soln = Solution()

lst_1 = [100,4,200,1,3,2] # 4
lst_2 = [0,3,7,2,5,8,4,6,0,1]
lst_3 = [0,1,2]

print(soln.longestConsecutive(lst_1))
print(soln.longestConsecutive(lst_2))
print(soln.longestConsecutive(lst_3))
