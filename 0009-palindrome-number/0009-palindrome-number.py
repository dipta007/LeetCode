class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rgtp = 1
        tmp = x
        while tmp:
            rgtp *= 10
            tmp //= 10
        
        rgtp //= 10

        tx = x
        while tx:
            lft = tx%10
            tx //= 10

            rgt = x // rgtp
            rgt = rgt%10
            rgtp //= 10

            if lft != rgt:
                return False

        return True
