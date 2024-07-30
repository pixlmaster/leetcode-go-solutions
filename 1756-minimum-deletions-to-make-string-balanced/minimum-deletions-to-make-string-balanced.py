class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        store the a to the right of each index and b to the left of each index
        min = as to the right and bs to the left
        """
        n = len(s)
        toLeftB = []
        currB = 0
        for idx, char in enumerate(s):
            toLeftB.append(currB)
            if char == "b":
                currB += 1
        currA = 0
        ans =float("inf")
        for idx in range(n - 1, -1,-1):
            # print(idx,ans,currA, toLeftB[idx])
            ans = min(ans,currA+toLeftB[idx])
            if s[idx] == "a":
                currA += 1
        
        if ans == float("inf"):
            return 0
        
        return ans
                
