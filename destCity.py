"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""

# Solution 1 (Using Set):

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
       s = set(p[0] for p in paths)
       for p in paths:
           if p[1] not in s:
               return p[1]

# Time Complexity = O(n) where n is the length on paths
# Space Complexity = O(c) where c is the number of cities

# Solution 2 (Using HashMap):

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityDict = {}
        for p in paths:
            cityDict[p[0]]  = p[1]
        for k,v in cityDict.items():
            if v not in cityDict:
                return v

# Time Complexity = O(n)
# Space Complexity = O(c)
