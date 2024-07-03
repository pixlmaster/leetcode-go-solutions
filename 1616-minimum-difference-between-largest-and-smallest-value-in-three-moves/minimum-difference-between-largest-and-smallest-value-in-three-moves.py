
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        # sort the array
        # largestPtr, smallestPtr
        # get the min value of 0,n-4, 1,n-3, 2, n-2 and 3, n-1
        n = len(nums)
        if n <=4:
            return 0
        nums.sort()
        ans = float("inf")
        ans = min(ans,nums[n-4]-nums[0])
        ans = min(ans,nums[n-3]- nums[1])
        ans = min(ans,nums[n-2]-nums[2])
        ans = min(ans,nums[n-1]- nums[3])
        
        return ans