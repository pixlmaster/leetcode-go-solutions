class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        n= len(s)
        for i in range(n):
            if i>0 and i<n-1 and s[i]==s[i-1] and s[i]==s[i+1]:
                continue
            else:
                ans +=s[i]
        return ans