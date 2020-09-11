"""

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return
        if val == root.val:
            return root
        elif  val < root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

# Time Complexity = O(n) A total of n nodes need to be traversed. Here, n represents the minimum number of nodes from the two given trees.

# Space complexity : O(n). The depth of the recursion tree can go upto n in the case of a skewed tree. In average case, depth will be O(logn).

