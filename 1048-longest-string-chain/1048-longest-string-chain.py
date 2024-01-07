class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        def predecessor(w1, w2):
            if len(w2) != len(w1) + 1:
                return False
            
            i, j = 0, 0
            while j < len(w2) and i < len(w1):
                if w2[j] == w1[i]:
                    j += 1
                    i += 1
                else:
                    j += 1
            
            return i == len(w1)

        @lru_cache
        def call(ind):
            if ind >= len(words):
                return 0
            
            res = 0
            for j in range(ind+1, len(words)):
                # print(ind, j)
                if predecessor(words[ind], words[j]):
                    res = max(res, 1 + call(j))
            return res

        res = 0
        # print(words)
        for i in range(len(words)):
            res = max(res, call(i) + 1)
            # print(i, res)

        return res
        