class Solution:
    def trailingZeroes(self, n: int) -> int:
        count5 = 0
        for num in range(n,4,-1):
            cnum = num
            while cnum % 5 == 0:
                count5+=1
                cnum = cnum//5
        
        return count5