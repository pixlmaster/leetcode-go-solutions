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
            # if we have already reached the target, we must have done the shortening in the prev loop
            # remove the first character which is guranteed to be significant
            # this opens up one more space to extend our candidate further
            if included == target :
                currfreq[s[start]]-=1
                included -=1
                start+=1


            # significant character
            if s[i] in currfreq :
                currfreq[s[i]] +=1
            else :
                currfreq[s[i]] = 1

            # increment the frequency of the significant character, if it is not already up to the mark
            if currfreq[s[i]] <= freq[s[i]] :
                included += 1

            # if the significant characters reacht the expected mark, try removing stuff from the start
            while included == target :
                if s[start] not in freq:
                    # remove non significant characters
                    start+=1
                elif  currfreq[s[start]] > freq[s[start]]:
                    # freely remove characters are more than expected
                    currfreq[s[start]] -=1
                    start+=1
                else:
                    # if you enocunter a significant charact4er, do not remove it , curr string is a canditate
                    if i-start<minLen:
                        minLen = i - start
                        ansStart = start
                    break
        if ansStart == -1 :
            return ""

        return s[ansStart:ansStart+minLen+1]
            



