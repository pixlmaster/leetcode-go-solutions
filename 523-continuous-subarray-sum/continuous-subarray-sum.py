class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # nums = nums %k and get max and min and prefix sum, with 0 as start
        # calculate prefix sum and hash it, search element by element up till max and min
        # if found then check the index , at least 2 elements need to be present
        n = len(nums)
        if n<=1:
            return False
        hmap = {}
        numMax, numMin = self.preProcess(nums,k, hmap)
        for sidx,num in enumerate(nums):
            for toSearch in range(num,numMax+1,k):
                # search for higher number present
                if toSearch in hmap:
                    hidx = hmap[toSearch]
                    if abs(hidx-sidx) >=2 and abs(nums[hidx] - nums[sidx])%k ==0:
                        return True
        
        return False
    
    def preProcess(self, nums: List[int], k  : int, hmap : dict[int,int]) :
        nums.insert(0,0)
        numMin = float("+inf")
        numMax = float("-inf")
        hmap[nums[0]] = 0
        for i in range(1,len(nums)):
            nums[i] = nums[i]%k
            nums[i] += nums[i-1]
            hmap[nums[i]] = i
            numMax = max(numMax,nums[i])
            numMin = min(numMin, nums[i])
        
        return numMax, numMin
            
            