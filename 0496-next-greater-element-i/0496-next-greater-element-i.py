class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = nums2[:]
        st = []
        ind = {}
        for j in range(len(nums2)-1, -1, -1):
            while len(st) > 0 and st[-1] < nums2[j]:
                st.pop()
            
            res[j] = -1 if len(st) == 0 else st[-1]
            st.append(nums2[j])
            ind[nums2[j]] = j
        
        ret = []
        for i in range(len(nums1)):
            cind = ind[nums1[i]]
            ret.append(res[cind])
        
        return ret
