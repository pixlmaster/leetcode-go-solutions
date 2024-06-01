class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0 
        for idx,char in enumerate(s) :
            if idx == len(s)-1:
                return ans
            ans +=abs( ord(char)-ord(s[idx+1]))
        
        return ans
            
        