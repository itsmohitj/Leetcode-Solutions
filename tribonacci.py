"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.


Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

"""

# Solution 1 : Memoization

class Solution:
    memo = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]

# Time Complexity = O(n)
# Space Complexity = O(n)

# Solution 2 : Tabulation

class Solution:
    def tribonacci(self, n: int) -> int:
        lookup = [0,1,1]
        for i in range(3,n+1):
            lookup.append(lookup[i-1] + lookup[i-2] + lookup[i-3])
        return lookup[n]

# Time Complexity = O(n)
# Space Complexity = O(n)
