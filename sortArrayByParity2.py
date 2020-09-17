"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        odd = 1
        even = 0
        for i in A:
            if i%2 == 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd +=2
        return res

# Time Complexity = O(n)
# Space Complexity = O(n)
