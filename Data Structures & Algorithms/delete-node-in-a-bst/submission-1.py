# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key) # want to delete node from right subtree and return that modified subtree back to root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key) # want to delete node from left subtree and return that modified subtree back to root
        else: # found node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: # left and right trees exist, find smallest value on the right to return
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val # give current root the value of smallest node, then delete that node
                root.right = self.deleteNode(root.right, curr.val)
        
        return root