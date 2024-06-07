class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse = 0
        store = x
        while x:
            last = x %10
            reverse = reverse*10 + last
            x = x//10
        # print(store,reverse)
        if store == reverse:
            return True
        
        return False
