class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # generate all possible subsets
        # iterate and check whether all are in the set or not
        n = len(s)
        wset = set()
        for word in wordDict :
            wset.add(word)

        dp = []
        for i in range(n):
            dp.append([])


        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1) :
                word = s[i:j]
                if not word in wset :
                    continue
                # if the word finishes the given input
                if j == n :
                    dp[i].append(word)
                    continue
                # if it does not, append it to the others
                for sent in dp[j] :
                    dp[i].append(word + " " + sent)
        return dp[0]
                    


        
        



            
        

        