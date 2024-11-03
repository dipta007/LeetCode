class Node:
    def __init__(self):
        self.ltr = {}
        self.total = 0

class Trie:
    def __init__(self):
        self.head = Node()
    
    def insert(self, w):
        curr = self.head
        for c in w:
            curr.total += 1
            if c not in curr.ltr:
                curr.ltr[c] = Node()
            curr = curr.ltr[c]
        curr.total += 1

    def find(self, tot):
        def dfs(curr):
            res = ""
            for k in curr.ltr.keys():
                if curr.ltr[k].total == tot:
                    nw = k + dfs(curr.ltr[k])
                    if len(nw) > len(res):
                        res = nw

            return res
        
        return dfs(self.head)
                
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tree = Trie()
        for w in strs:
            tree.insert(w)
        
        return tree.find(len(strs))