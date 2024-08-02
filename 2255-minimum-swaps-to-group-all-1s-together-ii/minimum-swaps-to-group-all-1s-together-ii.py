class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        count1 = count number of 1s
        sliding window with start from 0 and end at count1-1 -> n-1, count1-2
        number of 0s = number of swaps
        """
        count1 = 0
        for num in nums:
            if num == 1:
                count1 += 1
        if count1 == 0:
            return 0
        
        start =0
        end = count1
        count0 = 0
        for itr,num in enumerate(nums):
            if itr >=end:
                break
            if num == 0:
                count0+=1
        
        ans = count0
        
        n = len(nums)
        while start < n :
            # delete the start index and include the end index
            if nums[start] == 0:
                count0-=1
            if nums[(start+count1)%n] == 0:
                count0+=1
            ans = min(ans,count0)
            start+=1
        return ans
