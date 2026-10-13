# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # helper function isEqual
    def isEqual(self, t1, t2):
        if not t1 and not t2:
            return True
        if (t1 and not t2) or (t2 and not t1) or t1.val != t2.val:
            return False
        return self.isEqual(t1.left, t2.left) and self.isEqual(t1.right, t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not subRoot:
        #     return True
        if not root:
            return False

        if self.isEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)