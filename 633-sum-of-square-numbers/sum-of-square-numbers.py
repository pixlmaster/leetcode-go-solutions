
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        store = set()
        for num in range(0,c+1):
            if c - num*num < 0:
                break
            store.add(num*num)
            if c - num*num in store:
                return True
        
        
        return False