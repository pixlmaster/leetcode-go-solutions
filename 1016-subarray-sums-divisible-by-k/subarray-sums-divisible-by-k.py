class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        nums.insert(0,0)
        freq = {}
        n = len(nums)
        for i in range(n):
            nums[i] += nums[i-1]
            nums[i] = nums[i]%k
            if nums[i] not in freq :
                freq[nums[i]] = 1
            else:
                freq[nums[i]] +=1
        ans = 0
        for val in freq.values():
            if val >=2 :
                ans += (val*(val-1))//2
        
        return ans



            