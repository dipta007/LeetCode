class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        rm, rp, rg = 0, 0, 0
        tm, tp, tg = 0, 0, 0
        for i, w in enumerate(garbage):
            tm += travel[i]
            tp += travel[i]
            tg += travel[i]

            cm = w.count('M')
            if cm:
                rm += tm
                rm += cm
                tm = 0
            
            cp = w.count('P')
            if cp:
                rp += tp
                rp += cp
                tp = 0
            
            cg = w.count('G')
            if cg:
                rg += tg
                rg += cg
                tg = 0
        
        return rm + rp + rg