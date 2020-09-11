"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
       result, stack = [], []
       if not root:
           return None
       stack.append(root)
       while stack:
           root = stack.pop()
           result.append(root.val)
           stack.extend(reversed(root.children))
       return result

# Time Complexity = O(n), since n nodes need to be traversed.
# Space Complexity = O(n), max depth of stack can reach upto n.
