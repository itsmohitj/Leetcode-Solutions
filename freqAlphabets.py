"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1):
            s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s


# Time Complexity = O(n)
# Space Complexity = O(1)
