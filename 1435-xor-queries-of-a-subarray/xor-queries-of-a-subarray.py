class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        pre compute xors from left
        compute total xor
        """
        preCompute = []
        n = len(arr)
        curr = 0
        for i in range(n):
            curr = curr^arr[i]
            preCompute.append(curr)
        ans = []
        for query in queries:
            left = query[0]
            right = query[1]
            
            if left >0 :
                ans.append(preCompute[left-1]^preCompute[right])
            else:
                ans.append(preCompute[right])
            
        return ans