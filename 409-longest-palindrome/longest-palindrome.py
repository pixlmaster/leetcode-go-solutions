class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        for char in s:
            if not char in hmap :
                hmap[char] = 1
            else:
                hmap[char] +=1
        ans =0 
        for value in hmap.values():
            if value %2 ==0 :
                ans += value
            else:
                if ans%2==0:
                    ans+=value
                else:
                    ans+=value-1
        
        return ans

