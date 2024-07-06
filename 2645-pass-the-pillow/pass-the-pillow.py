class Solution:
    def passThePillow(self, n: int, k: int) -> int:
        k = k %(2*n-2)
        if k<n:
            return k+1
        k=k-n
        return n-1-k