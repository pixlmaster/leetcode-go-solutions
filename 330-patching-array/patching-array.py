class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        ans = 0
        i = 0
        l = len(nums)
        # all sums from [0,miss) can be made
        while miss <= n:
            if i < l and nums[i] <=miss:
                # if the number is smaller than the upper limit
                # the number will expand the max limit we can go to
                # since we can already make all elements smaller than < miss
                miss += nums[i]
                i+=1
            else:
                # the number from miss to the next greatest cannot be formed
                # add miss to the list(optimal case)
                miss += miss
                ans +=1
        
        return ans