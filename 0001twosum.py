from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3,3], 6))
