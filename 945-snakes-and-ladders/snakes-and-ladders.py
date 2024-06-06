
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # do a bfs from the 1st node
        # children of a node are, the next 6 blocks and any block connecting these 6 via a ladder
        # snakes can be efficient too , since they might allow us to take a better ladder
        # do level order traversal do find the min distance
        return self.bfs(board)

    def bfs(self, board: List[List[int]]) ->int:
        n = len(board)
        visited= set()
        q = deque()
        q.append((1,0))
        while q :
            label, step = q.popleft()
            r,c = self.getCoordFromNum(label,n)
            if board[r][c] !=-1:
                label = board[r][c]
            if label == n*n:
                return step
            
            for i in range(1,7):
                newl = label + i
                if newl <= n*n and newl not in visited:
                    visited.add(newl)
                    q.append((newl,step+1))
        return -1
                
    
    def getCoordFromNum(self, num, n):
        r  = int((num-1)/n)
        c = (num-1) % n
        if r % 2 == 0:
            return n-1-r, c
        else:
            return n-1-r, n-1-c
