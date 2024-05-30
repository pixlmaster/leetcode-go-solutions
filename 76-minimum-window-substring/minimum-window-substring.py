class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for char in t :
            if char not in freq :
                freq[char] = 1
            else :
                freq[char] += 1
        

        n = len(s)
        target = len(t)

        start = 0
        ansStart = -1
        included = 0
        minLen = pow(10,6)
        currfreq = {}
        for i in range(n):
            if s[i] not in freq :
                continue
            # if included == target :
            #     while s[start]  :
            #         if s[start] not in freq:
            #             start+=1
            #         else:
            #             included -=1
            #             currfreq[s[start]]-=1
            #             start+=1

            if included == target :
                currfreq[s[start]]-=1
                included -=1
                start+=1


            # significant character
            if s[i] in currfreq :
                currfreq[s[i]] +=1
            else :
                currfreq[s[i]] = 1


            if currfreq[s[i]] <= freq[s[i]] :
                included += 1


            # print(s[start:i+1])
            # print(currfreq,included)
            # reached a point where the substring has all of the characters or more
            while included == target :
                if s[start] not in freq:
                    start+=1
                elif  currfreq[s[start]] > freq[s[start]]:
                    currfreq[s[start]] -=1
                    start+=1
                else:
                    if i-start<minLen:
                        minLen = i - start
                        ansStart = start
                        # print(s[start:i+1], s[ansStart:ansStart+minLen], ansStart,minLen)
                    break
        if ansStart == -1 :
            return ""

        return s[ansStart:ansStart+minLen+1]
            



