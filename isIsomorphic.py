"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Input: s = "egg", t = "add"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for i in range(len(s)):
            if s[i] in h1:
                if h1[s[i]] != t[i]:
                    return False
            elif t[i] in h2:
                return False
            else:
                h1[s[i]] = t[i]
                h2[t[i]] = s[i]
        return True

# Time Complexity = O(n)
# Space Complexity = O(n)
