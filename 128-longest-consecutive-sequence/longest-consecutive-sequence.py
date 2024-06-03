class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        hmap = {}
        for num in nums:
            if num in hmap and hmap[num] == -1:
                continue
            longest = 1
            cnum=num +1
            while cnum in numset:
                if cnum in hmap and hmap[cnum]>0:
                    longest+=hmap[cnum]
                    break
                longest+=1
                hmap[cnum] = -1
                cnum+=1
            hmap[num] = longest
        longest = 0
        for val in hmap.values():
            longest = max(longest,val)
        return longest
        
