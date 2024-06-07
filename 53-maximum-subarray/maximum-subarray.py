class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        curr= 0
        for num in nums:
            curr+= num
            ans =max(ans,curr)
            if curr < 0:
                curr = 0
        return ans