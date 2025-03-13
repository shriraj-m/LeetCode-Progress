"""1372. Longest ZigZag Path in a Binary Tree"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0

        def zzdfs(node, count, direction):
            self.maxLength = max(self.maxLength, count)

            if node.left != None: # left exists
                if direction != "left":
                    zzdfs(node.left, count+1, "left")
                else:
                    zzdfs(node.left, 1, "left")
        
            if node.right != None: # right exists
                if direction != "right":
                    zzdfs(node.right, count+1, "right")
                else:
                    zzdfs(node.right, 1, "right")
            
        zzdfs(root, 0, "start")
        return self.maxLength

            
