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
        if not root:
            return TreeNode(val)
        node = root
        parent = root

        while True:
            parent = node
            if node.val < val:
                node = node.right
                if not node:
                    parent.right = TreeNode(val)
                    break
            else:
                node = node.left
                if not node:
                    parent.left = TreeNode(val)
                    break

        return root
