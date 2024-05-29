class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        curr = 0  
        ans = n+1
        start = 0

        for i in range(n) :
            curr += nums[i]
            while curr >= target :
                # print(start,i)
                ans = min(ans,i-start+1)
                curr -= nums[start]
                start+=1
        if ans > n :
            return 0
        return ans