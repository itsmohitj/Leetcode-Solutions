"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0 for i in range(n)]
        left,right = 0, n-1
        for i,v in enumerate(A):
            if A[i] % 2 == 0:
                res[left] = A[i]
                left += 1
            else:
                res[right] = A[i]
                right -= 1
        return res

# Time Complexity = O(n)
# Space Complexity = O(n)
