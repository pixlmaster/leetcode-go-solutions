type queue struct {
    q []int
    front int
    back int
}

func createQ() *queue {
    return &queue{make([]int,0) , 0 ,0}
}

func (q *queue)push(elem int) {
    q.q = append(q.q,elem)
    q.back++
}

func (q *queue)pop() {
    q.front++
}

func (q *queue)top() int{
    if q.isEmpty() {
        return -1
    }
    return q.q[q.front]
}

func (q *queue)isEmpty() bool{
    return q.front == q.back
}


func deckRevealedIncreasing(deck []int) []int {
    n := len(deck)
    q := createQ()
    sort.Ints(deck)
    for i:=0 ; i<n;i++{
        q.push(i)
    }

    res := make([]int,n)

    for _, card := range deck {
		idx := q.top()
		q.pop()
		res[idx] = card

		if !q.isEmpty() {
			q.push(q.top())
            q.pop()
		}
	}
    return res
}
