class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = self.binSearchInsert(matrix,target)
        if idx < 0 :
            return False
        
        return self.binSearch(matrix[idx], target)
    
    def binSearch(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        
        return False
    
    def binSearchInsert(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)

        start = 0
        end = row-1
        
        while start<=end:
            mid =(start+end)//2
            if matrix[mid][0] == target:
                return mid
            
            if target > matrix[mid][0] :
                if mid == row-1:
                    return row-1
                elif target < matrix[mid+1][0]:
                    return mid
                start = mid +1
            else :
                end = mid - 1
                
        return -1