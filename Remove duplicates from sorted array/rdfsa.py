from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for i in range(len(nums) - 1):
            # if seen is empty or number is not in seen
                # add to seen
                # change array in place at arr[len(seen)]
            # if number is in seen
                # do nothing
            if (len(seen) == 0) or nums[i] not in seen:
               seen.append(nums[i])
               nums[len(seen)] = seen[i]
        return [len(nums), nums] 
solution = Solution()

print(solution.removeDuplicates([1,2,3,3,3]))
