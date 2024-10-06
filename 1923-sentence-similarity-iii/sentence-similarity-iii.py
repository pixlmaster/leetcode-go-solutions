class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1tokens = sentence1.split()
        s2tokens = sentence2.split()
        return self.checkInsertIns2(s1tokens, s2tokens) or self.checkInsertIns2(s2tokens, s1tokens)

    def checkInsertIns2(self, token1: list[str], token2: list[str]) -> bool:
        print("Start")
        # find the break point
        i1,i2 = 0,0
        n1,n2 = len(token1),len(token2)
        while i1<n1 and i2<n2 and token1[i1]==token2[i2]:
            # print("matched" , token1[i1], token2[i2])
            i1+=1
            i2+=1
        matchesLeft = n2 - i2
        i1 = n1 - matchesLeft
        while i1>=0 and i1<n1 and i2<n2 and token1[i1]==token2[i2]:
            # print("matched" , token1[i1], token2[i2])
            i1+=1
            i2+=1
        return i1==n1 and i2==n2
        