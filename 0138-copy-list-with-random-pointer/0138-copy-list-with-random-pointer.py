"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        def call(c1):
            if c1 is None:
                return None

            if c1 in node_map:
                return node_map[c1]
            
            curr = Node(c1.val)

            node_map[c1] = curr
            curr.next = call(c1.next)
            curr.random = call(c1.random)

            return curr

        return call(head)