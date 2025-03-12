"""872. Leaf-Similar Trees"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, values):
            if node:
                if node.left == None and node.right == None: # no children
                    values.append(node.val)
                # depth first search through tree
                dfs(node.left, values)
                dfs(node.right, values)

        leaf_1 = []
        leaf_2 = []
        # dfs on both
        dfs(root1, leaf_1)
        dfs(root2, leaf_2)
        # compare both
        return leaf_1 == leaf_2

