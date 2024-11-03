class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = {
            "6": "9",
            "9": "6",
            "8": "8",
            "1": "1",
            "0": "0"
        }
        m_num = []
        for c in num:
            m_num.append(mirror.get(c, "K"))
        
        m_num = "".join(m_num[::-1])
        return m_num == num