class Solution:
    def alienOrder(self, words: List[str]) -> str:
        from collections import defaultdict, deque
        adj = defaultdict(set)
        
        words = [f"${w}" for w in words]
        
        for w1, w2 in zip(words, words[1:]):
            l, r = 0, min(len(w1), len(w2)) - 1
            cmn = 0
            while l <= r:
                m = (l + r) // 2
                if w1[:m+1] == w2[:m+1]:
                    l = m + 1
                    cmn = m
                else:
                    r = m - 1
            
            if cmn != min(len(w1), len(w2)) - 1:
                adj[w1[cmn+1]].add(w2[cmn+1])
            else:
                if len(w1) > len(w2):
                    return ""

        indeg = defaultdict(int)
        for k, ns in adj.items():
            for v in ns:
                indeg[v] += 1
        
        dq = deque()
        chars = set()
        for w in words:
            for i in range(1, len(w)):
                c = w[i]
                chars.add(c)
        for c in chars:
            if indeg[c] == 0:
                dq.append(c)

        res = ""
        while dq:
            u = dq.popleft()
            res += u

            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    dq.append(v)

        if sum(indeg.values()) > 0:
            return ""
        return res