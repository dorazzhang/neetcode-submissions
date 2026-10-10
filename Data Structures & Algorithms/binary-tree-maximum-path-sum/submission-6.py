# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max path sum of any path
        # doesnt need to include root
        # negative numbers? yes
        # undirected tree
        max_path = float("-inf")

        def dfs(node): # max path sum with node as root
            nonlocal max_path
            if not node.left and not node.right: # if leaf, best value is itself
                max_path = max(max_path, node.val)
                return node.val
            elif not node.left:
                right_max = dfs(node.right)
                max_path = max(max_path, node.val, node.val + right_max, right_max)
                return max(node.val, node.val + right_max)
            elif not node.right:
                left_max = dfs(node.left)
                max_path = max(max_path, node.val, node.val + left_max, left_max)
                return max(node.val, node.val + left_max)
            else:
                left_max = dfs(node.left)
                right_max = dfs(node.right)
                max_path = max(max_path, node.val, node.val + left_max, left_max, node.val + right_max, right_max, node.val + left_max + right_max)
                return max(node.val, left_max + node.val, right_max + node.val)
        
        return max(dfs(root), max_path)    