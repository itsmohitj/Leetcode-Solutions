'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

'''

# Asymmetric List Solution :

class Solution:
    def sumZero(self, n: int) -> List[int]:
         return list(range(1, n)) + [n * (1 - n) // 2]

# Symmetric List Solution:

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-(n//2), 0)) + [0]*(n % 2) + list(range(1, n//2 + 1))
