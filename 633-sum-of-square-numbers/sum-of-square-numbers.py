
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for num in range(0,c+1):
            toSearch = c - num*num
            if toSearch < 0:
                break
            if math.sqrt(toSearch)%1 ==0:
                return True
        
        
        return False