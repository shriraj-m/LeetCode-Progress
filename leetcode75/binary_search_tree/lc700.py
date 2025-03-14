"""700. Search in a Binary Search Tree"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.val == val:
            return root

        # if current value is greater than what we are looking for, we go left
        # else, we would go right, (rules of a BST)
        if root.val > val: 
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)