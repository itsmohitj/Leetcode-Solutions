"""
Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

# Solution 1:

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Time complexity : O(n+m) in the average case and O(n×m) in the worst case when load factor is high enough.

# Space complexity : O(n+m) in the worst case when all elements in the arrays are different.

# Solution 2:

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = []
        for i in nums1:
            if i not in hash and i in nums2:
                hash.append(i)
        return hash

# Time Complexity = O(n) where n is the length of nums1
# Space Complexity = O(n)
