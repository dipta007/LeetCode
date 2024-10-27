"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = [0] * 104

        def call(curr):
            if curr is None:
                return None
            
            clone = Node(curr.val)
            visited[curr.val] = clone
            for n in curr.neighbors:
                if n and visited[n.val] != 0:
                    clone.neighbors.append(visited[n.val])
                else:
                    clone.neighbors.append(call(n))
            
            return clone
        
        return call(node)