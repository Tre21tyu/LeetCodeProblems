from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # {1: 2, 2: 1}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # ({1: 2, 2: 1}, [[], [2], [1], []])
        for n, c in count.items():
            freq[c].append(n)

        res = []
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return count, res, freq

solution = Solution()

print(solution.topKFrequent([1, 1, 2, 2], 1))
print(solution.topKFrequent([1, 1, 2, 2, 3, 3, 4, 4], 2))
