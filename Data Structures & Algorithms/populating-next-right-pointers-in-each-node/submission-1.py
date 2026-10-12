"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs where you visit nodes one level at a time
        # aka preorder? (node, left, right)

        # queue so we know which level we're on

        queue = deque()
        if root:
            queue.append(root)

        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node
        
        return root