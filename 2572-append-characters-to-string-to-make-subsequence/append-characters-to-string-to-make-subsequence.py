class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        slen = len(s)
        tlen = len(t)
        sptr = 0
        tptr = 0
        lastMatched = -1

        while sptr<slen and tptr < tlen :
            if s[sptr] == t[tptr]:
                lastMatched = tptr
                sptr+=1
                tptr+=1
                continue
            sptr+=1
        if lastMatched == -1 :
            return tlen
        return tlen - lastMatched -1

                