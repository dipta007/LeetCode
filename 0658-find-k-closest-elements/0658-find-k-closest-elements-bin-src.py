class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        lft_ind = -1
        arr = arr + [arr[-1] + 1000000000]
        while l <= r:
            m = (l + r) // 2
            # print(l, m, r, x, (arr[m] + arr[m+k]) / 2)
            if x <= (arr[m] + arr[m+k]) / 2:
                lft_ind = m
                r = m - 1
            else:
                l = m + 1
            
        return arr[lft_ind:lft_ind+k]

