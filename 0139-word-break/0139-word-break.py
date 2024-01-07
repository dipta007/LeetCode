class Node:
    def __init__(self):
        self.child = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = Node()
            curr = curr.child[w]
        curr.end = True
    
    @lru_cache
    def dfs(self, i, w, curr):
        if i >= len(w):
            return curr.end
        
        res = False
        if curr.end == True:
            res = self.dfs(i, w, self.root)
        
        if w[i] in curr.child:
            res = res or self.dfs(i+1, w, curr.child[w[i]])
        return res

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tree = Trie()
        for w in wordDict:
            tree.insert(w)
        
        return tree.dfs(0, s, tree.root)
        