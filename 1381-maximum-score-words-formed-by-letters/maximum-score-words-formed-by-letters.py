class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        wordMap , letterMap = self.freqMap(words,letters,score)
        # print(wordMap)
        # print(letterMap)
        n = len(words)
        total = pow(2,n)
        ans = 0
        for i in range(total) :
            temp = i
            itr = 0
            currMap = [0]*26
            while temp > 0 :
                if temp & 1 == 1 :
                    for j in range(len(currMap)):
                        currMap[j] += wordMap[itr][j]
                    prune, curr = self.anyGreater(currMap,letterMap,score) 
                    if prune :
                        break
                    ans = max(ans,curr)
                itr+=1
                temp = temp >> 1

        return ans


    def anyGreater(self, freq1 : List[int], freq2 : List[int], score: List[int]) -> Tuple[bool, int] :
        curr = 0
        for i in range(len(freq1)) :
            if freq1[i] > freq2[i] :
                return True , -1
            curr += freq1[i]*score[i]
        return False, curr

    def freqMap(self, words: List[str], letters : List[str],score: List[int]) -> Tuple[List[List[int]], List[int]]:
        freqMap = []
        for idx, word in enumerate(words) :
            freqMap.append([0]*26)
            for char in word :
                freqMap[idx][ord(char) - ord('a')]  += +1

        charMap = [0]*26
        for idx, letter in enumerate(letters) :
            charMap[ord(letter) - ord('a')]+=1

        return freqMap, charMap

        