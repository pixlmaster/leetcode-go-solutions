class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        n = len(s)
        if n== 0 :
            return 0
        
        ans = 1
        start = 0

        for i in range(n):
            if not s[i] in freq :
                freq.add(s[i])
                ans = max(ans,i-start+1)
                continue
            # repeated character
            while s[i] in freq :
                freq.remove(s[start])
                start+=1    
            freq.add(s[i])
            # ans = max(ans,i-start+1)
        
        return ans
        