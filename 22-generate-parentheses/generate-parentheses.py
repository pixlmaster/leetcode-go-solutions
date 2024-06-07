class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking takes in open avail, right avail
        # use right only if right> left
        # left can be used anytime
        ans = []
        self.recurse(n,n,"",ans)
        return ans

    def recurse(self,op: int, close: int, curr: str, ans : List[str]) ->None:
        if op ==0 and close ==0:
            ans.append(curr)
            return
        # use open
        if op > 0:
            self.recurse(op-1,close, curr +"(", ans)
        
        if close>0 and close >op :
            self.recurse(op,close-1, curr +")", ans)
        