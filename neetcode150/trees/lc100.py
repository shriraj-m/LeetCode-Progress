# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True # both are null, so same
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
        # traverse both in order
        # self.res1 = []
        # self.res2 = []
        # def traverse(root, list_type):
        #     if not root:
        #         list_type.append(None)
        #         return None
        #     list_type.append(root.val)
        #     traverse(root.left, list_type)
        #     traverse(root.right, list_type)
        
        # traverse(p, self.res1)
        # traverse(q, self.res2)
        # print(self.res1)
        # print(self.res2)
        # if self.res1 == self.res2:
        #     return True
        # else:
        #     return False
        