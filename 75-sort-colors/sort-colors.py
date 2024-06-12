class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # startPtr points at the start
        # endPtr points at the end
        # while currPtr< endPtr
        # if 0, then swap with start and increment start
        # if 1, do nothing
        # if 2, then swap with end and decrement end

        n = len(nums)
        startPtr = 0
        endPtr = n - 1
        currPtr = startPtr
        while currPtr <= endPtr:
            # print(startPtr,currPtr,endPtr)
            if nums[currPtr] == 0:
                temp = nums[startPtr]
                nums[startPtr] = nums[currPtr]
                nums[currPtr] = temp
                startPtr += 1
            elif nums[currPtr] == 1:
                currPtr+=1
            else:
                temp = nums[endPtr]
                nums[endPtr] = nums[currPtr]
                nums[currPtr] = temp
                endPtr -= 1
            currPtr = max(currPtr,startPtr)
