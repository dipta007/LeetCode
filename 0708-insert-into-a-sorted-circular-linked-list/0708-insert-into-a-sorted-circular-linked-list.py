"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            nc = Node(insertVal)
            nc.next = nc
            return nc

        if head.next == head:
            nnode = Node(insertVal)
            head.next = nnode
            nnode.next = head
            return head

        prev = head
        curr = head.next

        while True:
            insert = False
            if (insertVal >= prev.val and insertVal <= curr.val):
                insert = True
            elif curr.val < prev.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True
            
            if insert:
                nnode = Node(insertVal)

                prev.next = nnode
                nnode.next = curr
                break
            
            prev = prev.next
            curr = curr.next

            if prev == head: break
        
        prev.next = Node(insertVal, curr)
        return head