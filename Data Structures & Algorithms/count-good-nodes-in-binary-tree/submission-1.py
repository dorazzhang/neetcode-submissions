# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good if path from root to it contains no nodes w value greater

        # traverse down path dfs, storing the greatest seen node
        # if curr_node greater than greatest seen node, increment 1

        def dfs(node, maximum): # returns number of good nodes under node
            if not node: # empty tree has no good nodes
                return 0
            
            if node.val >= maximum: # curr_node is good
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val) # add 1 to count and continue with left and right with new max
            else: # curr_node is not good
                return dfs(node.left, maximum) + dfs(node.right, maximum)
        
        return dfs(root, float("-inf"))



        