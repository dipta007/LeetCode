class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def call(i, p, curr):
            if p < 0:
                return
            if i == n:
                if p == 0 and curr:
                    nonlocal res
                    res.append(curr[:])
                return

            call(i+1, p+1, curr + '(')
            call(i+1, p-1, curr + ')')

        n = n + n
        call(0, 0, "")
        return res