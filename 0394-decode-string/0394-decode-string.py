class Solution:
    def decodeString(self, s: str) -> str:
        def call(l, r):
            num = 0
            i = l
            res = ""
            # print(l, r, s[l:r+1])
            while i <= r:
                c = s[i]
                if c.isnumeric():
                    num = num * 10 + int(c)
                elif c == '[':
                    ll = i
                    rr = i
                    p = 0
                    while True:
                        if s[rr] == '[':
                            p += 1
                        elif s[rr] == ']':
                            p -= 1
                        if p == 0:
                            break
                        rr += 1
                    
                    res = res + num * call(ll+1, rr-1)
                    num = 0
                    i = rr
                elif c != ']':
                    res += c

                i += 1

            return res

        s = "1[" + s + "]"
        return call(0, len(s)-1)

# 1[3[a2[b]]]