class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return self.bsearch(nums,1,100)

    def bsearch(self,nums: List[int], s: int, e : int) -> int:
        if s <0 or e >100 or s>e :
            return -1
        mid = int((s+e)/2)
        n = len(nums)
        idx = self.arrbsearch(nums, len(nums), 0, n-1, mid)
        if n-idx == mid :
            return mid
        if n-idx > mid :
            return self.bsearch(nums,mid+1,e)
        if n- idx < mid :
            return self.bsearch(nums,s,mid-1)

    def arrbsearch(self,nums: List[int],n: int, s: int, e : int, elem: int) -> int :
        mid = int((s +e)/2)
        if nums[mid] == elem :
            if mid == 0 or nums[mid-1]<elem:
                return mid
            if nums[mid-1] == elem:
                return self.arrbsearch(nums,n,s,mid-1,elem)
        elif nums[mid] > elem :
            if mid == 0 or nums[mid-1]<elem:
                return mid
            return self.arrbsearch(nums,n,s,mid-1,elem)
        if mid == n-1:
            return n
        return self.arrbsearch(nums,n,mid+1,e,elem) 
            
