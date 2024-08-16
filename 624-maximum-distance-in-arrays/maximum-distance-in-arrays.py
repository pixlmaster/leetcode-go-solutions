class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """
        for each array,
        pick the smallest elem, calc the max difference from mins and maxes of other elements
        pick th largest
        """
        ans = 0
        cand = arrays[0][0]
        cand1 = arrays[0][-1]
        for idx in range(1,len(arrays)):
                ans = max(ans,abs(cand - arrays[idx][-1]))
                ans = max(ans,abs(cand1 - arrays[idx][0]))
                cand = min(cand,arrays[idx][0])
                cand1 = max(cand1, arrays[idx][-1])
        
        return ans
"""
[5,6]
[1,2,3,4,5,6]
"""