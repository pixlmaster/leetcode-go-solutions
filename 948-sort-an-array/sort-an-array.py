class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergeSort(nums)
        return nums


    def mergeSort(self, nums : list[int]) -> None:
        if len(nums) <=1 :
            return

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        self.mergeSort(left)
        self.mergeSort(right)

        ## merge step
        itrl = 0
        itrr=0
        lenl = len(left)
        lenr = len(right)

        while itrl < lenl and itrr < lenr :
            # print(left)
            # print(right)
            # print(itrl, lenl, itrr, lenr)
            if left[itrl] <= right[itrr] :
                nums[itrl+itrr] = left[itrl]
                itrl+=1
            else :
                nums[itrr + itrl] = right[itrr]
                itrr+=1

        while itrl < lenl:
            nums[itrl+itrr] = left[itrl]
            itrl+=1

        while itrr < lenr:
            nums[itrl+itrr] = right[itrr]
            itrr+=1


