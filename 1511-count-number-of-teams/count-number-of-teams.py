class Solution:
    def numTeams(self, rating: list[int]) -> int:
        """
        go over each element and store the elements greater than this element and less than the element after the current index
        """
        n = len(rating)
        lmap = {}
        gmap = {}
        for idx in range(n):
            curr = rating[idx]
            lmap[curr] = 0
            gmap[curr] = 0
            for nextIdx in range(idx + 1, n):
                next = rating[nextIdx]
                if next > curr:
                    gmap[curr] += 1
                else:
                    lmap[curr] += 1
        ans = 0
        for i1 in range(n-2):
            s1 = rating[i1]
            for i2 in range(i1+1,n-1):
                s2 = rating[i2]
                if s2 > s1 :
                    ans += gmap[s2]
                else:
                    ans += lmap[s2]
        
        return ans
