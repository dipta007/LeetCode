class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        res = ""
        ind = 0
        while len(res) < len(word1) + len(word2):
            if ind % 2 == 0:
                if i < len(word1):
                    res += word1[i]
                    i += 1
                else:
                    res += word2[j]
                    j += 1
            else:
                if j < len(word2):
                    res += word2[j]
                    j += 1
                else:
                    res += word1[i]
                    i += 1
            ind += 1
        return res