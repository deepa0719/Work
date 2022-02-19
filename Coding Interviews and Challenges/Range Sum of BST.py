# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sums = 0
        def dfs(node):
            if not node:
                return
            if low<= node.val <= high:
                self.sums+=node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return self.sums
        
