class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans1 = {}
        ans2 = {}
        words1 = s1.split()
        words2 = s2.split()
        ans = set()
        
        for word in words1:
            if word not in ans1:
                ans1[word] = 1
            else:
                ans1[word] += 1
        for word in words2:
            if word not in ans2:
                ans2[word] = 1
            else:
                ans2[word] += 1
        
        for word in words1:
            if ans1[word] == 1 and word not in ans2:
                ans.add(word)
        for word in words2:
            if ans2[word] == 1 and word not in ans1:
                ans.add(word)
        return list(ans)