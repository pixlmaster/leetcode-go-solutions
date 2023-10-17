func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
    if(n==1){
        return true
    }


    var children = make([][2]int,n)
    var parent = make(map[int]int)
    for i:=0 ; i < n ;i++ {
        children[i][0] = leftChild[i]
        children[i][1] = rightChild[i]
        // fmt.Println(i)
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
    // fmt.Printf("finding the parent\n")
    // find parent
    parentFound := false
    p :=-1
    for i:=0 ; i < n ;i++ {
        _, ok := parent[i]
        if !ok {
            if !parentFound && (children[i][0]!=-1 || children[i][1]!=-1 ) {
                parentFound = true
                p = i
            } else if parentFound && (children[i][0]!=-1 || children[i][1]!=-1 ) {
                return false
            }
        }
    }
    if !parentFound{
        return false
    }

    var visited = make(map[int]bool)

    // do dfs
    dfs(p, children, visited)
    for i:=0 ; i < n ;i++ {
        _ , ok := visited[i]
        if !ok {
            return false
        }

    }
    
    return true
}

func dfs(node int, children [][2]int , visited map[int]bool){
    if node == -1 {
        return
    }
    visited[node] = true
    dfs(children[node][0], children, visited)
    dfs(children[node][1], children, visited)
}