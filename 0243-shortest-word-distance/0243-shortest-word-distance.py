class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = len(wordsDict)
        ind1, ind2 = -1, -1
        for i, v in enumerate(wordsDict):
            if v == word1:
                ind1 = i
            if v == word2:
                ind2 = i
            
            if ind1 > -1 and ind2 > -1:
                res = min(res, abs(ind1 - ind2))
        return res