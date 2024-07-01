class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        while i <= len(arr)-3:
            if arr[i]%2 == 0:
                i+=1
                continue
            if arr[i+1]%2 ==0:
                i+=2
                continue
            if arr[i+2]%2 == 0:
                i+=3
                continue
            return True
        return False