# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # dfs
        # stack = [(p, q)]
        # while stack:
        #     node1, node2 = stack.pop()

        #     if not node1 and not node 2:
        #         continue
        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False
        #     stack.append((node1.right, node2.right))
        #     stack.append((node1.left, node2.left))
        # return True

        #bfs

        queue1 = deque()
        queue2 = deque()
        queue1.append(p)
        queue2.append(q)
        
        while queue1 and queue2:
            for i in range(len(queue1)):
                node1 = queue1.popleft()
                node2 = queue2.popleft()

                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return True

            
        