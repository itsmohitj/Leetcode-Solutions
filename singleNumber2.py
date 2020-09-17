"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        for key, val in hash.items():
            if val != 3:
                return key

# Time Complexity = O(n)
# Space Complexity = O(n)
