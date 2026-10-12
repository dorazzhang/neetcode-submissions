# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # BST and a value to insert
        # return root node after insertion

        # left subtree is smaller than parent
        # right subtree is greater than parent

        # go down the tree, left or right depending on the value youre comparing. when you hit null, you know you can insert there 
        # track parent so you can set parent.left or parent.right as the new node
        node = root
        parent = root

        while node:
            parent = node
            if node.val < val:
                node = node.right
            else:
                node = node.left
        
        node = TreeNode(val)
        if not parent:
            return node
        elif parent.val < val:
            parent.right = node
        else:
            parent.left = node

        return root
