class Node:
    def __init__(self):
        self.ltr = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, w):
        curr = self.root
        for c in w:
            if c not in curr.ltr:
                curr.ltr[c] = Node()
            curr = curr.ltr[c]
        curr.end = True
    
    def search(self, w):
        # print(len(w))
        @cache
        def call(i, curr):
            if not curr:
                return False
            if i == len(w):
                # print(i, len(w), curr.end)
                return curr.end
            
            res = False
            res = res or call(i+1, curr.ltr.get(w[i], None))
            
            if curr.end:
                res = res or call(i, self.root)

            return res
        return call(0, self.root)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tree = Trie()
        for w in wordDict:
            tree.insert(w)
        
        return tree.search(s)