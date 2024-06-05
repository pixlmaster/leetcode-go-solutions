class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if not letter in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["*"] =""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        ans = []
        row = len(board)
        col = len(board[0])

        for word in words:
            trie.insert(word)

        for i in range(row):
            for j in range(col):
                self.dfs(board,trie.root,i,j,row, col, "",ans)
        
        return ans

    
    def dfs(self,board: List[List[str]], node: Trie, r :int, c:int,row:int,col:int, curr: str, res: List[str]):
        # print(node)
        # print("*" in node)
        # print(curr)
        if "*" in node:
            res.append(curr)
            del node["*"]
        if r<0 or r >= row or c<0 or c >= col:
            return
        
        temp = board[r][c]
        if not temp in node:
            return
        children = node[temp]
        # pruning


        board[r][c] = "#"
        self.dfs(board,children,r+1,c,row,col,curr+temp,res)
        self.dfs(board,children,r-1,c,row,col,curr+temp,res)
        self.dfs(board,children,r,c+1,row,col,curr+temp,res)
        self.dfs(board,children,r,c-1,row,col,curr+temp,res)
        board[r][c] = temp