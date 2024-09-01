class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        """
        construct m*n from 1d array
        """
        orignalLen = len(original)
        if orignalLen != m*n:
            return []

        ans = []
        for r in range(m):
            ans.append(original[r*n:(r+1)*n])
        
        return ans
