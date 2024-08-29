class Solution:

    def removeStones(self, stones: list[list[int]]) -> int:
        """
        count number of clusters
        a cluster is all possible rows and cols that can be reached from one stone(not necessarily connected)
        """
        numStones = len(stones)
        # hash the number of stones according to r or c
        rowStones = {}
        colStones = {}
        for stone in stones:
            r = stone[0]
            c = stone[1]
            if r not in rowStones:
                rowStones[r] = [stone]
            else:
                rowStones[r].append(stone)

            if c not in colStones:
                colStones[c] = [stone]
            else:
                colStones[c].append(stone)

        clusters = 0
        visited = set()
        for stone in stones:
            r = stone[0]
            c = stone[1]
            if (r, c) not in visited:
                self.dfs(r, c, rowStones, colStones, visited)
                clusters += 1

        return numStones - clusters
    
    def dfs(self, r : int, c : int, rowStones : dict[int,list[list[int]]], colStones : dict[int,list[list[int]]], visited : set[(int,int)]) -> None:
        # return if already visited
        if (r,c) in visited:
            return 
        # mark visited
        visited.add((r,c))
        
        # visit all row stones
        for stone in rowStones[r]:
            self.dfs(stone[0],stone[1], rowStones,colStones,visited)

        # visit all col stones
        for stone in colStones[c]:
            self.dfs(stone[0],stone[1], rowStones,colStones,visited)
            
