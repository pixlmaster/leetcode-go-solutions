class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums :
            xor ^= num

        cxor = xor
        mask = 1
        while cxor & mask !=mask :
            mask= mask << 1
        ans =[0]*2
        for num in nums:
            if num & mask > 0:
                ans[0]^=num
            else:
                ans[1]^=num
        return ans
