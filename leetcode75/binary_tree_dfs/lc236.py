"""236. Lowest Common Ancestor of a Binary Tree"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            # base case
            if node == None:
                return
            
            # current node is p or q, so return
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            # if left and right return non-nulls, then the current node is the LCA
            if left and right:
                return node
            
            # else, return non-null child 
            if left:
                return left
            else:
                return right
            
        return dfs(root)

