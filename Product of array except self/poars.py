from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numbers = nums[:]
        # List of prefixes
        prefix = []
        postfix = []
        result = [] 

        product = 1

        for num in numbers:
            product *= num
            prefix.append(product)

        # product = 1

        for num in reversed(numbers):
            product *= num
            postfix.append(product)

        return prefix, postfix
    # , postfix

solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))


