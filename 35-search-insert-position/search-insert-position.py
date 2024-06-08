class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1

        while start<=end:
            mid = (start+end)//2
            # print(start,mid,end)
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                if mid == n-1:
                    return n
                elif target< nums[mid+1]:
                    return mid+1
                start = mid+1
            else:
                if mid == 0:
                    return 0
                elif target> nums[mid-1]:
                    return mid 
                end= mid -1

        return -1
            
            