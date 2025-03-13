""" 437. Path Sum III """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # set a hash map to keep track of prefix sums
        prefixes = {0: 1} # base case to have 1 way of a 0 sum (no nodes)

        def dfs(node, current_sum):
            if node == None:
                return 0
            current_sum += node.val
            # grab the current sum - target sum from dict, if no exist it is 0
            num_paths = prefixes.get(current_sum - targetSum, 0)
            # update hashmap
            prefixes[current_sum] = prefixes.get(current_sum, 0) + 1
            # recursively iterate down left and right
            num_paths += dfs(node.left, current_sum)
            num_paths += dfs(node.right, current_sum)
            # backtrack while removing current sum from hashmap
            prefixes[current_sum] -= 1

            return num_paths
        
        return dfs(root, 0)
