class Node:
    def __init__(self):
        self.letter = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, w):
        curr = self.root
        for c in w:
            if c not in curr.letter:
                curr.letter[c] = Node()
            curr = curr.letter[c]
        curr.end = True
    
    def find(self, w):
        curr = self.root
        cnt = 0
        for c in w:
            if c not in curr.letter:
                break
            curr = curr.letter[c]
            cnt += 1
        return cnt

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(w) for w in arr1]
        arr2 = [str(w) for w in arr2]
        tree = Trie()
        for w in arr1:
            tree.insert(w)
        
        res = 0
        for w in arr2:
            res = max(res, tree.find(w))
        
        return res