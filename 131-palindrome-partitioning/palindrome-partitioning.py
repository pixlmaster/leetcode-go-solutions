class Solution:
    def constructdp(self, s: str) -> List[List[int]]:
        dp = []
        n  = len(s)
        for i in range(n) :
            dp.append([0]*n)
        # for palindrome of length l
        for l in range(n) :
            # starting at ith position
            for i in range(n-l) :
                if l == 0 :
                    # 1 letter words
                    dp[i][i+l] = 1
                    continue
                if l == 1 or l == 2 :
                    # 2/3 letter words
                    if s[i] == s[i+l]:
                        dp[i][i+l] = 1
                    else :
                        dp[i][i+l] = -1
                    continue
                # >3 letter words
                if s[i] != s[i+l] :
                    dp[i][i+l] = -1
                else :
                    dp[i][i+l] = dp[i+1][i+l-1]
        return dp
                
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n  = len(s)
        dp = self.constructdp(s)
        self.recurse(s,dp,n,0,[],ans)
        return ans

    def recurse(self,s :str , dp : List[List[int]], n: int, start: int, curr: List[str], ans: List[List[str]]):
        if start >= n :
            # print(curr, len(curr))
            if len(curr) == 0 :
                return
            
            ans.append(curr)
            return
        for l in range(n-start) :
            if dp[start][start+l]  > 0 :
                currCopy = copy.deepcopy(curr)
                currCopy.append(s[start:start+l+1])
                self.recurse(s,dp,n,start+l+1, currCopy,ans)   

        return 


                
                
