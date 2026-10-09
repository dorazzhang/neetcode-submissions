# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # arr = []
        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return arr[k - 1]

        count = k
        res = root.val
        if count == 0:
            return res

        def dfs(node):
            nonlocal count, res
            if not node:
                return
            
            dfs(node.left)
            count -= 1
            if count == 0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res

        