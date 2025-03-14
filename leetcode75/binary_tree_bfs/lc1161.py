"""1161. Maximum Level Sum of a Binary Tree"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        node_list = []
        def bfs(node, level, node_list):
            if node == None:
                return

            if len(node_list) <= level:
                node_list.append([]) # append empty array if len is same as level
            
            node_list[level].append(node.val) # add value into list based on level

            bfs(node.left, level + 1, node_list)
            bfs(node.right, level + 1, node_list)
        
        bfs(root, 0, node_list)
        print(node_list)

        # iterate through lists and calculate sums. return level of the sum with the max
        max_sum_level = 0
        max_sum = float('-inf')
        index = 1
        for l in node_list:
            # l is list level index
            current_sum = sum(l)
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_level = index
            index += 1
        
        return max_sum_level
        



