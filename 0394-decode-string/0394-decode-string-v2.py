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

        # s = "1[" + s + "]"
        # return call(0, len(s)-1)

        stack = []
        for c in s:
            # print(c, stack)
            if c == ']':
                curr_s = ""
                while stack[-1] != '[':
                    curr_s += stack.pop()
                stack.pop() # pop [
                
                curr_num = 0
                p = 1
                while stack and stack[-1].isnumeric():
                    curr_num += int(stack.pop()) * p
                    p *= 10
                
                s = curr_s * curr_num

                for cs in s[::-1]:
                    stack.append(cs)
            else:
                stack.append(c)

        # print(stack)
        return "".join(stack)