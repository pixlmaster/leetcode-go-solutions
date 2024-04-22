
type queue struct{
    q []string
    front int
    back int
}

func createQueue(n int) *queue{
    return &queue{make([]string,n),0,0}
}

func (q *queue) enq(val string) {
    q.q[q.back] = val
    q.back++
}

func (q *queue) deq() {
    q.front++
}

func (q *queue) fron() string {
    if q.empty(){
        return ""
    }
    return q.q[q.front]
}

func (q *queue) empty() bool {
  return q.front==q.back
}

func possib(curr string) []string {
    ans := make([]string,8)

    for i:=0 ; i<4 ; i++ {
        s := curr[i]
        if s=='0'{
            ans[2*i] = curr[0:i] + "9" + curr[i+1:4]
            ans[2*i +1] = curr[0:i] + "1" + curr[i+1:4]
        } else if s=='9' {
            ans[2*i] = curr[0:i] + "8" + curr[i+1:4]
            ans[2*i +1] = curr[0:i] + "0" + curr[i+1:4]
        } else{
            ans[2*i] = curr[0:i] + string(s-1) + curr[i+1:4]
            ans[2*i +1] = curr[0:i] +  string(s+1)+ curr[i+1:4]
        }
    }
    return ans
}


func openLock(deadends []string, target string) int {
    // convert deadends to set
    visited := make(map[string]bool)
    for i:=0 ; i<len(deadends) ; i++ {
        visited[deadends[i]] = true
    }
    qu := createQueue(10*10*10*10)
    ans := 0
    // do bfs
    qu.enq("0000")
    if visited["0000"] == true {
        return -1
    }
    visited["0000"] = true
    for ; !qu.empty() ; {
        newqu := createQueue(10*10*10*10)
        for ; !qu.empty() ; {
            toVisit := qu.fron()
            // fmt.Println(toVisit, qu.back)
            qu.deq()
            if toVisit == target {
                return ans
                break;
            }
            children := possib(toVisit)
            //visit unvisited children
            for i := 0 ; i<8 ;i++{
                if !visited[children[i]] {
                    newqu.enq(children[i])
                    visited[children[i]] = true
                }
            }
        }
        qu = newqu
        ans++
    }
    

    return -1


}


