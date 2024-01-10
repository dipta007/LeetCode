class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        nn = int(sqrt(n))

        lft = []
        rgt = []

        for i in range(1, nn+1):
            if n % i == 0:
                lft.append(i)
                if n // i != i:
                    rgt.append(n // i)
        
        # print(lft, rgt)
        n = k
        if n > len(lft) + len(rgt):
            return -1

        # print(n)
        if n <= len(lft):
            return lft[n-1]

        n -= len(lft)
        # print(n)
        n = len(rgt) - n + 1
        # print(n)
        return rgt[n-1]