"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        first, last = None, None

        def call(curr):
            if curr is None:
                return

            call(curr.left)

            nonlocal first, last
            if last is None:
                first = curr
            else:
                last.right = curr
                curr.left = last
            
            last = curr

            call(curr.right)

        call(root)

        last.right = first
        first.left = last

        return first
