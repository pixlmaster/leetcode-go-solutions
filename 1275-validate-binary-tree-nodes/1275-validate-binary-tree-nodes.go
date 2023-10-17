func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
    if(n==1){
        return true
    }
    var parent = make(map[int]int)
    for i:=0 ; i < n ;i++ {
        // ensure each node has only 1 parent
        if leftChild[i] != -1 {
             _ , ok := parent[leftChild[i]]
            if ok {
                return false
            } else {
                parent[leftChild[i]] = i
            }
        }

        if rightChild[i] != -1 {
            _ , ok := parent[rightChild[i]]
            if ok {
                return false
            } else {
                parent[rightChild[i]] = i
            }
        }
    }

    parentFound := false
    p :=-1
    for i:=0 ; i < n ;i++ {
        _, ok := parent[i]
        if !ok {
            if !parentFound && (leftChild[i]!=-1 || rightChild[i]!=-1 ) {
                parentFound = true
                p = i
            } else if parentFound && (leftChild[i]!=-1 || rightChild[i]!=-1 ) {
                return false
            }
        }
    }
    if !parentFound{
        return false
    }

    var visited = make(map[int]bool)

    // do dfs
    dfs(p, leftChild, rightChild, visited)
    for i:=0 ; i < n ;i++ {
        _ , ok := visited[i]
        if !ok {
            return false
        }

    }
    
    return true
}

func dfs(node int, leftChild []int, rightChild []int, visited map[int]bool){
    if node == -1 {
        return
    }
    visited[node] = true
    dfs(leftChild[node], leftChild,rightChild , visited)
    dfs(rightChild[node], leftChild,rightChild , visited)
}