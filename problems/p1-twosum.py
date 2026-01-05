from typing import List

class Solution:
    def twoSum(self, nums, target) -> List[int]:
        found: dict = {}
        for (i, v) in enumerate(nums):
            if (target - v) in found:
                return [found[target - v], i]
            else:
                found[v] = i


sol = Solution()
answer = sol.twoSum([2, 7, 11, 15], 9)
print(answer)
