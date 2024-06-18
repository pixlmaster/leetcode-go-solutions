
type Job struct {
	diff   int
	profit int
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	n := len(difficulty)
	var jobs []Job
	for i := 0; i < n; i++ {
		jobs = append(jobs, Job{difficulty[i], profit[i]})
	}
	sort.Ints(difficulty)
	sort.Slice(jobs, func(i, j int) bool {
		if jobs[i].diff < jobs[j].diff {
			return true
		} else if jobs[i].diff == jobs[j].diff {
			return jobs[i].profit>jobs[j].profit
		}
		return false
	})
	prefixMax := make([]int,n)
	curr := -1
	for i :=0; i<n ; i++{
		if jobs[i].profit > curr{
			curr = jobs[i].profit
		}
		prefixMax[i] = curr
	}
    // fmt.Println(jobs)
	ans :=0
	for _,w := range worker{
		idx := sort.SearchInts(difficulty,w)
        if idx == n || difficulty[idx]!=w{
            idx--
        }
        if idx <0 {
            continue
        }
        // fmt.Println("worker", w, "insert at", idx)
		ans +=prefixMax[idx]
	}

	return ans
}