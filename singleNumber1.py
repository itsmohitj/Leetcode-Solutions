"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

"""

# Solution 1 (Using Hash):

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        for key, val in hash.items():
            if val == 1:
                return key

# Time Complexity = O(n)
# Space Complexity = O(n)

# Solution 2 (Using XOR):

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

# Time Complexity = O(n)
# Space Complexity = O(1)


# Solution 3 (Using Set):

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)

# Time Complexity = O(n)
# Space Complexity = O(1)
