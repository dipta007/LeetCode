import bisect

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def check(x, y):
            print(x, y, y <= 0.5 * x + 7)
            if y <= 0.5 * x + 7:
                return False
            if y > x:
                return False
            if y > 100 and x < 100:
                return False
            return True

        cnt = 0
        ages.sort()
        for i in range(len(ages)):
            x = ages[i]

            y_r = int(0.5 * x + 7) + 1
            if x < 100:
                y_r = min(y_r, 100)
            # if x > 100:
            #     y_r = max(y_r, 100)
            
            if y_r > x: continue
            x = min(x, ages[i])


            lft = bisect.bisect_left(ages, y_r)
            rgt = bisect.bisect_right(ages, x)
            rgt -= 1

            print(y_r, x, lft, rgt, rgt-lft)
            cnt += (rgt - lft)


        return cnt