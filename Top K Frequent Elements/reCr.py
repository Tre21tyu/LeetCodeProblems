from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # For all of the numbers in nums
        for n in nums:
            # To the count dictionary, use .get() to goto the key, n, in the dictionary
            # Then, increment its value by 1. If it's not in the dicitonary,
            # Put it in the dicitonary and give it a default value of 0.
            count[n] = 1 + count.get(n, 0)

        #  in that list that corresponds to the key. In that index (c)
        #  append the value at count[n].
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):    
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return count, freq, res

solution = Solution()

print(solution.topKFrequent([1, 2, 2, 2] ,1))
