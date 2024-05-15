type point struct {
    x int
    y int
}

type queue struct {
    q []point
    front int
    back int
}

func createQueue() queue{
    return queue{make([]point,0),0,0}
}

func (qu *queue) deq() point {
    if qu.front > qu.back{
        qu.back++
    }
    return qu.q[qu.back-1]  
}

func (qu *queue) enq(p point) {
    qu.q = append(qu.q,p)
    qu.front++;
}

func (qu *queue) show() {
    if qu.empty(){
        return
    }
    for i := qu.back ; i< qu.front ; i++ {
        fmt.Printf("%d ", qu.q[i])
    }
    fmt.Println()
}

func (qu *queue) top() point {
    if qu.front > 0 {
        return qu.q[qu.front-1]
    }
    return point{-1,-1}
}

func (qu *queue) empty() bool {
    if qu.front<=qu.back {
        return true
    }
    return false
}

func (qu *queue) num() int {
    return qu.front-qu.back
}

func maximumSafenessFactor(grid [][]int) int {
    n:= len(grid)
    if grid[0][0] == 1 || grid[n-1][n-1] == 1{
        return 0
    }

    dist := make([][]int,n)
    // put all the thieves here
    for i:=0 ; i< n ; i++ {
        dist[i] = make([]int,n)
    }
    multiBFS(grid,dist)
    minimum := 0
    maximum := min(dist[0][0],dist[n-1][n-1])
    return bin(dist,minimum,maximum,maximum,n)
}

func multiBFS(grid [][]int, dist [][]int) {
    q1 := createQueue()
    n := len(grid)
    visited := make([][]bool,n)
    // put all the thieves here
    for i:=0 ; i< n ; i++ {
        visited[i] = make([]bool,n)
        for j:=0 ; j<n ; j++ {
            if grid[i][j] == 1 {
                p := point{i,j}
                q1.enq(p)
                visited[p.x][p.y] = true

            }
        }
    }
    
    level :=0
    // level order BFS traversal
    for ; !q1.empty() ;{
        toPop := q1.num()
        // q1.show()
        // fmt.Println(toPop,q1.back,q1.front)
        for i:=0 ; i< toPop ; i++ {
            p := q1.deq()
            dist[p.x][p.y] = level
            // fmt.Println("level", level,"x:", p.x,"y:", p.y)
            // enqueue children
            if p.x - 1 >=0 && !visited[p.x-1][p.y]{
                visited[p.x-1][p.y] = true
                q1.enq(point{p.x-1,p.y})
            }
            if p.x + 1 <n && !visited[p.x+1][p.y]{
                visited[p.x+1][p.y] = true
                q1.enq(point{p.x+1,p.y})
            }
            if p.y - 1 >=0 && !visited[p.x][p.y-1]{
                visited[p.x][p.y-1] = true
                q1.enq(point{p.x,p.y-1})
            }
            if p.y + 1 <n && !visited[p.x][p.y+1]{
                visited[p.x][p.y+1] = true
                q1.enq(point{p.x,p.y+1})
            }
        }
        level++

    }
    // for i:=0 ; i<n ; i++ {
    //     for j:=0; j< n ; j++ {
    //         fmt.Printf("%d ", dist[i][j])
    //     }
    //     fmt.Println()
    // }
}

func bin(dist [][]int, minimum int,maximum int, ciel int, n int) int{
    // fmt.Println(minimum,maximum,ciel)
    if minimum > maximum {
        return -1
    }

    mid := (minimum + maximum)/2
    withMid := dfs(dist, mid, n)
    // fmt.Println("mid ", mid)

    // fmt.Println("withMid ", withMid)
    if mid == ciel && withMid {
        return mid
    }
    withGreaterMid := dfs(dist, mid+1, n)
    // fmt.Println("withGreaterMid ", withGreaterMid)
    // posssible to traverse with mid but not the next greatest one
    if withMid && !withGreaterMid {
        return mid
    }
    // could not traverse with mid
    if !withMid {
        return bin(dist,minimum,mid-1,ciel,n)
    }
    if withMid {
        return bin(dist,mid +1, maximum , ciel,n)
    }
    return -1
}

func dfs(dist [][]int, limit int, n int) bool{
    visited := make([][]bool, n)
    for i:=0 ; i<n ; i++ {
        visited[i] = make([]bool, n)
    }
    return recurse(dist,limit,0,0,n,visited)
}

func recurse(dist [][]int,limit int,x int,y int, n int, visited [][]bool) bool {
    if x==n-1 &&y == n-1 {
        return true
    }
    visited[x][y] = true
    //visit children
    left,top,right,bot := false,false,false,false

    if x - 1 >=0 && !visited[x-1][y] && dist[x-1][y]>=limit{
        top = recurse(dist,limit,x-1,y,n,visited)
    }
    if x + 1 <n && !visited[x+1][y] && dist[x+1][y]>=limit{
        bot = recurse(dist,limit,x+1,y,n,visited)
    }
    if y - 1 >=0 && !visited[x][y-1]&& dist[x][y-1]>=limit{
        left = recurse(dist,limit,x,y-1,n,visited)
    }
    if y + 1 <n && !visited[x][y+1]&& dist[x][y+1]>=limit{
        right = recurse(dist,limit,x,y+1,n,visited)
    }
    // fmt.Println("dfs",x,y,limit, left,right,top,bot)

    if left||top||bot|| right {
        return true
    }
    return false

}

func min(x,y int) int {
    if x < y {
        return x
    }
    return y
}