# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        # dfs in tree
        # when left and right become none, check if target == node.val
        # if it does, we return None to the parent

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.left and not node.right:
                if node.val == target:
                    return None

            return node
        
        dfs(root)
        return root if root.val != target else None
        