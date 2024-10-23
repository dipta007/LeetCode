"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def call(curr):
            if curr is None:
                return None

            if curr == p or curr == q:
                return curr
            
            lft = call(curr.left)
            rgt = call(curr.right)

            if lft and rgt:
                return curr
            
            return lft if lft is not None else rgt
        
        root = p
        while root.parent: root = root.parent
        return call(root)