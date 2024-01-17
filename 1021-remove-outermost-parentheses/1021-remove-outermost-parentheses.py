class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        res = ""
        nw = ""
        for v in s:
            nw += v
            if v == '(':
                st.append(1)
            else:
                st.pop()
                if len(st) == 0:
                    res += nw[1:-1]
                    nw = ""
        return res