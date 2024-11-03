class Node:
    def __init__(self):
        self.ltr = {}
        self.end = False

class Trie:
    def __init__(self):
        self.head = Node()
    
    def insert(self, w):
        curr = self.head
        for c in w:
            if c not in curr.ltr:
                curr.ltr[c] = Node()
            curr = curr.ltr[c]
        curr.end = True
    
    def get(self):
        res = []
        def call(curr, folder):
            end = False
            if curr.end:
                end = True
                nonlocal res
                res.append(folder[:])
            
            for c in curr.ltr.keys():
                if not end and c == '/':
                    call(curr.ltr[c], folder + c)
                elif c != '/':
                    call(curr.ltr[c], folder + c)
        
        call(self.head, "")
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tree = Trie()
        for f in folder:
            tree.insert(f)

        return tree.get()