class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_c, prev_cnt = chars[0], 1
        i = 1
        j = 1
        while i < len(chars):
            while i < len(chars) and chars[i] == prev_c:
                prev_cnt += 1
                i += 1

            if prev_cnt > 1:
                prev_cnt = str(prev_cnt)
                k = 0
                while k < len(prev_cnt):
                    chars[j] = prev_cnt[k]
                    j += 1
                    k += 1
            
            # either i == len(chars) or new char
            if i != len(chars):
                prev_c = chars[i]
                prev_cnt = 0
                chars[j] = prev_c
                j += 1
        
        return j
            

