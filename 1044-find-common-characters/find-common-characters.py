class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hmap = {} 
        for char in words[0]:
            if not char in hmap:
                hmap[char] = 1
            else:
                hmap[char]+=1
        for i in range(1,len(words)):
            word = words[i]
            tmap = {}
            for char in word:
                if not char in tmap:
                    tmap[char] = 1
                else:
                    tmap[char]+=1
            for char, freq in hmap.items():
                if not char in tmap:
                    hmap[char] = 0
                else:
                    hmap[char] = min(freq,tmap[char])

        ans =[]    
        for char,val in hmap.items():
            ans.extend([char]*val)
        
        return ans