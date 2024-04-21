func validPath(n int, edges [][]int, source int, destination int) bool {
    if source == destination{
        return true
    }
    emap := make([][]int,n)

    for _ , edge := range edges {
        emap[edge[0]] = append(emap[edge[0]], edge[1])  
        emap[edge[1]] = append(emap[edge[1]], edge[0])
    }
    visited := make([]bool,n)

    return dfs(source,destination,emap,visited)

}

func dfs(source int, destination int, emap [][]int, visited []bool) bool{
    if source == destination {
        return true
    }

    visited[source] = true

    for _, neighbour := range emap[source] {
        if !visited[neighbour] {
            if dfs(neighbour, destination,emap,visited){
                return true
            }
        }
    }
    return false
}