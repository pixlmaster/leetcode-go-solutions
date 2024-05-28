class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
     
        ans = 0
        curr =0
        i = 0
        start= 0
        # sliding window
        while i<n:
            # print(i)
            curr += abs(ord(s[i]) - ord(t[i]))
            # move the back of the window forward
            while curr> maxCost :
                curr -= abs(ord(s[start]) - ord(t[start]))
                start+=1
            ans = max(ans,i-start+1)
            i+=1


        return ans
