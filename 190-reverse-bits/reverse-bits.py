class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            lastbit = n&1
            ans =ans << 1
            ans +=lastbit
            n = n >> 1

        
        return ans