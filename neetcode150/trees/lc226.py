# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        

        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left) # call left tree
        self.invertTree(root.right) # call right tree

        return root
        