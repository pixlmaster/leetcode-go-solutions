class Solution:
    def numTeams(self, rating: list[int]) -> int:
        """
        go over each element and store the elements greater than this element and less than the element after the current index
        """
        n = len(rating)
        gmap = {}
        for idx in range(n):
            curr = rating[idx]
            gmap[curr] = 0
            for nextIdx in range(idx + 1, n):
                if rating[nextIdx] > curr:
                    gmap[curr] += 1
        ans = 0
        for i1 in range(n-2):
            s1 = rating[i1]
            for i2 in range(i1+1,n-1):
                s2 = rating[i2]
                if s2 > s1 :
                    ans += gmap[s2]
                else:
                    ans += n-i2-1 - gmap[s2]
        
        return ans
