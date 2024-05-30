class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = {}
        for word in words :
            if word in freq :
                freq[word]+=1
            else :
                freq[word] = 1
        
        ans = set()

        n = len(s)
        wlen = len(words[0])
        total = len(words)*wlen
        visited = [False]*n

        for i in range(n-wlen+1):
            if visited[i] :
                continue
            word = s[i:i+wlen]
            # if word is not part of set
            if word not in freq :
                continue
            start = i

            currFreq = {}
            j = i
            while j < n - wlen +1:
                visited[j] = True
                word = s[j:j+wlen]
                # valid word
                if word in freq:
                    if word in currFreq:
                        currFreq[word]+=1
                    else:
                        currFreq[word] = 1
                    while currFreq[word] > freq[word]:
                        toRemove = s[start:start+wlen]
                        currFreq[toRemove]-=1
                        start += wlen

                    if j-start + wlen == total :
                        ans.add(start)
                else:
                    if j-start == total:
                        ans.add(start)
                    break
                j+=wlen
            i = start
                    
        return ans