"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot, right = n - 2, n - 1

        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1

        if pivot == -1:
            nums.reverse()
            retur

        while right > pivot and nums[right] <= nums[pivot]:
            right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        nums[pivot+1:] = nums[pivot+1:][::-1]

# Time Complexity = O(n)
# Space Complexity = O(1)
