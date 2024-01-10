class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        ind = 0
        for v in pushed:
            while ind < len(popped) and st and st[-1] == popped[ind]:
                ind += 1
                st.pop()
            
            st.append(v)

        while ind < len(popped) and st and st[-1] == popped[ind]:
            ind += 1
            st.pop()

        return ind == len(popped)