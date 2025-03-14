"""199. Binary Tree Right Side View"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []
        def bfs(node, level, node_list):
            if node == None:
                return

            if len(node_list) <= level:
                node_list.append([])
            
            node_list[level].append(node.val)

            bfs(node.left, level+1, node_list)
            bfs(node.right, level+1, node_list)
        
        bfs(root, 0, node_list)
        if len(node_list) == 0:
            return node_list

        res_list = []
        for l in node_list:
            res_list.append(l[-1])
        
        return res_list
        
