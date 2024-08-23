class Solution:
    def findComplement(self, num: int) -> int:
        p = 0
        ans = 0
        while num :
            if num % 2 == 0:
                ans += pow(2,p)
            num = num//2
            p+=1
        return ans