class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import Counter
        counter = Counter(wordList)

        def get_adj(w):
            prev = ""
            for i in range(len(w)):
                c = w[i]
                after = w[i+1:]
                for ni in range(ord('a'), ord('z') + 1):
                    nc = chr(ni)
                    if c != nc:
                        nw = prev + nc + after
                        if nw in counter:
                            yield nw

                prev += c
            

        from collections import deque, defaultdict
        dq = deque()

        dq.append((beginWord, 0))
        vis = defaultdict(int)
        while dq:
            uw, ud = dq.popleft()
            if uw == endWord:
                return ud + 1
            for v in get_adj(uw):
                if vis[v] == 0:
                    dq.append((v, ud +1))
                    vis[v] = 1
        
        return 0
