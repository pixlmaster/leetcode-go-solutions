
func exist(board [][]byte, word string) bool {
    // handle corner cases
    m := len(board)
    if m == 0 {
        return false
    }
    n := len(board[0])
    if n == 0 {
        return false
    }

    // visited stores whether the node has been visited already in the current traversal
    visited := make([][]bool, m)
    for i := 0 ; i < m ;i++ {
        visited[i] = make([]bool, n)
    }

    prune := make([][]map[int]int, m)
    for i := 0 ; i < m ;i++ {
        prune[i] = make([]map[int]int, n)
        for j := 0 ; j< n ; j++ {
            prune[i][j] = make(map[int]int)
        }
    }

    for i:=0 ; i < m ; i++ {
        for j := 0 ; j<n ; j++ {
            if traverse(board,visited,m,n,i,j, word, prune) {
                return true
            }
        }
    }

    return false

}

func traverse(board [][]byte, visited[][]bool,m int, n int, i int, j int, word string, prune [][]map[int]int) bool{
    strLen := len(word)
    // base cases for recursion
    if strLen == 0 {
        return true
    }
    // current element does not match the first one
    if board[i][j] != word[0] {
        prune[i][j][strLen] = -1
        return false
    }

    value, found := prune[i][j][strLen]
    if found {
        if value == -1 {
            return false
        } else if value == 1 {
            visited[i][j] = true
            return true
        }
    }

    // if we reach here, that means 1st letter matched
    subStr := word[1:strLen]
    // set current node as visited
    visited[i][j] = true
    if strLen == 1 {
        prune[i][j][strLen] = 1
        return true
    }


    // visit top
    if i > 0 && !visited[i-1][j] && traverse(board,visited,m,n,i-1,j,subStr , prune) {
        return true
    }
    // left
    if j > 0 && !visited[i][j-1] && traverse(board,visited,m,n,i,j-1, subStr, prune) {
        return true
    }
    // right
    if j < n-1 && !visited[i][j+1] && traverse(board,visited,m,n,i,j+1, subStr, prune){
        return true
    }
    // bottom
    if i < m-1 && !visited[i+1][j] && traverse(board,visited,m,n,i+1,j, subStr, prune){
        return true
    }
    // if none can be found, set it back to unvisited
    visited[i][j] = false
    return false        
}