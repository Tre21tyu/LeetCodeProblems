from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {id: occur}
        freq_dict = {}
        most_freq = []
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1

        freq_dict_keys = list(freq_dict.keys())

        return freq_dict_keys[:k]

solution = Solution()

print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))

```

```
