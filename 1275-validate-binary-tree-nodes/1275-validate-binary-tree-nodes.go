func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
    if(n==1){
        return true
    }
    var allChildren = make(map[int]bool)
    for i:=0 ; i < n ;i++ {
        allChildren[leftChild[i]] = true
        allChildren[rightChild[i]] = true
    }

    parentFound := false
    p :=-1
    for i:=0 ; i < n ;i++ {
        _, ok := allChildren[i]
        if !ok {
            if !parentFound{
                parentFound = true
                p = i
            } else {
                return false
            }
        }
    }
    if !parentFound{
        return false
    }

    var visited = make(map[int]bool)

    // do dfs
    if !dfs(p, leftChild, rightChild, visited){
        return false
    }
    for i:=0 ; i < n ;i++ {
        _ , ok := visited[i]
        if !ok {
            return false
        }

    }
    
    return true
}

func dfs(node int, leftChild []int, rightChild []int, visited map[int]bool) bool{
    if visited[node] == true {
        return false
    }
    if node == -1 {
        return true
    }
    visited[node] = true
    return (dfs(leftChild[node], leftChild,rightChild , visited) && dfs(rightChild[node], leftChild,rightChild , visited))
}