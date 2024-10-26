class SparseVector:
    def __init__(self, nums: List[int]):
        self.colset = dict()
        self.cols = []
        self.vals = []
        for i, v in enumerate(nums):
            if v:
                self.colset[i] = len(self.cols)
                self.cols.append(i)
                self.vals.append(v)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for c, v in zip(vec.cols, vec.vals):
            if c in self.colset:
                res += (v * self.vals[self.colset[c]])
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)