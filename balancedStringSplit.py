"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        r_count = 0
        count = 0
        for i in s:
            if i == 'L':
                l_count+=1
            else:
                r_count+=1
            if l_count == r_count:
                count+=1
        return count

# Time Complexity = O(n)
# Space Complexity = O(1)
