class Solution:
    def checkStraightLine(self, C: List[List[int]]) -> bool:
        if len(set([x for x, y in C])) == 1 or len(set([y for x, y in C])) == 1:
            return True

        [x1, y1] = C[0]
        [x2, y2] = C[1]

        def get_slope(x1, y1, x2, y2):
            m1 = (y2 - y1)
            m2 = (x2 - x1)
            m = math.gcd(m1, m2)

            if m == 0: m = 1
            m1 //= m
            m2 //= m

            if (m1 < 0 and m2 < 0) or (m1 > 0 and m2 < 0):
                m1 *= -1
                m2 *= -1
            return m1, m2

        m1, m2 = get_slope(x1, y1, x2, y2)
        # print(x1, y1, x2, y2)
        # print(m1, m2)
        for [x3, y3] in C[2:]:
            m3, m4 = get_slope(x2, y2, x3, y3)

            # print(m3, m4)
            if m3 != m1 or m4 != m2:
                return False
        
        return True