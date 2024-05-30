class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start=0
        ans = []
        n= len(nums)
        for end in range(n) :
            if end==n-1 or nums[end+1]!=nums[end]+1:
                if end==start :
                    ans.append(str(nums[start]))
                else :
                    ans.append(str(nums[start]) + "->" + str(nums[end]))
                start = end+1
        return ans
                    
