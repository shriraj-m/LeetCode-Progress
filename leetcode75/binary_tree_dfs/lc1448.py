"""1448. Count Good Nodes in Binary Tree"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_seen):
            if node == None:
                return 0
            # check if there is a good node
            if node.val >= max_seen:
                good = 1
            else:
                good = 0
            
            new_max_seen = max(max_seen, node.val)

            return good + dfs(node.left, new_max_seen) + dfs(node.right, new_max_seen)

        return dfs(root, float('-inf'))