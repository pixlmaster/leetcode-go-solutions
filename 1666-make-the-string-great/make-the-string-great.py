class Solution:
    def makeGood(self, s: str) -> str:
        diff = abs(ord('A') - ord('a'))
        i = 0
        while i < len(s)-1:
            currDiff = abs(ord(s[i+1]) - ord(s[i]))
            if diff == currDiff:
                s = s[:i] + s[i+2:]
                if i!=0 :
                    i-=1
                continue
            i+=1
        
        return s

        