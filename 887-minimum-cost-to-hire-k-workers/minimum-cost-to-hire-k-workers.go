func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
    n := len(quality)
    workers := make([]worker,n)
    for i:=0; i< n ; i++ {
        workers[i].eff = float64(wage[i])/float64(quality[i])
        workers[i].qual = quality[i]
    }
    sort.Slice(workers, func(i,j int)bool {
        return workers[i].eff < workers[j].eff
    })

    ans := float64(1000000001)
    h := NewHeap()
    totalQual :=0
    for i:=0 ;i<n ;i++ {
        // push elements until elements in the heap reach k
        totalQual += workers[i].qual
        heap.Push(h, workers[i].qual)
        // fmt.Println("pushed ", workers[i].qual)

        // if we have more elements than k, pop the max quality one
        if h.Len() > k {
            removed := heap.Pop(h)
            // fmt.Println("removed ", removed)
            totalQual -= removed.(int)
        }
        // if we reach k elements calculate the minCost and update the ans
        // calculating ratio after we reach k elements ensure that the largest of the K ratios are picked
        // so that the threshold is crossed
        if h.Len() == k {
            temp := workers[i].eff * float64(totalQual)
            if ans > temp {
                ans = temp
            }
        }
    }
    return ans

}

type worker struct{
    eff float64
    qual int
}

type MaxHeap []int

func (m MaxHeap)Len() int {
    return len(m)
}


func (m MaxHeap)Less(i,j int) bool {
    return m[i] > m[j]
}

func (m MaxHeap)Swap(i,j int) {
    m[i] = m[i]^m[j]
    m[j] = m[j]^m[i]
    m[i] = m[j]^m[i]
}

func (m *MaxHeap)Push(val interface{}) {
    *m = append(*m,val.(int))
}

func (m *MaxHeap)Pop() interface{}{
    n:= len(*m)
    temp := (*m)[n-1]
    *m = (*m)[0:n-1]
    return temp
}

// Create a new heap
func NewHeap() *MaxHeap {
    h := &MaxHeap{}
    heap.Init(h)
    return h
}