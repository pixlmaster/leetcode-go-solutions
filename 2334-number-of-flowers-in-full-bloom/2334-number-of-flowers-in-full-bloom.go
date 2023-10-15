import "sort"

func fullBloomFlowers(flowers [][]int, people []int) []int {
    n := len(flowers)
    var start = make([]int,n)
    var end = make([]int,n)

    for row :=0 ; row < n ; row++ {
        start[row] = flowers[row][0]
        end[row] = flowers[row][1]
    }

    sort.Ints(start)
    sort.Ints(end)


    for itr:=0 ; itr<len(people) ; itr++{
        people [itr] = findBloom(people[itr],start,end, n)
    }

    return people
}

func findBloom(target int, start []int, end []int, n int) int {
    bloom := binSearchStart(target,start, 0, n-1, n)
    unbloom := binSearchEnd(target,end, 0, n-1, n)
    return bloom - unbloom
}

func binSearchStart(target int, start []int, s int, e int, n int) int{
    if s > e || s<0 || e>=n{
        return -1
    }
    mid := (s+e)/2

    // found
    if start[mid] == target {
        // last element or not repeated
        if mid == n-1 || start[mid+1] != target {
            return mid+1
        }
        // search right
        return binSearchStart(target, start, mid+1, e, n)
    } else if start[mid] < target {
        if mid == n-1 {
            return mid+1
        } else if start[mid+1] > target {
            return mid + 1
        }
        return binSearchStart(target, start, mid+1, e, n)
    }
    if mid == 0 {
        return 0
    } else if start[mid-1] < target{
        return mid- 1 +1
    }
    return binSearchStart(target,start, s, mid-1,n)

}

func binSearchEnd(target int, end []int, s int, e int, n int) int{
    if s > e || s<0 || e>=n{
        return -1
    }
    mid := (s+e)/2

    // found
    if end[mid] == target {
        // last element or not repeated
        if mid ==0 {
            return 0
        }
        if end[mid-1] != target {
            return mid- 1 + 1
        }
        // search right
        return binSearchEnd(target, end, s, mid-1, n)
    } else if end[mid] < target {
        if mid == n-1 {
            return mid+1
        } else if end[mid+1] > target {
            return mid + 1
        }
        return binSearchEnd(target, end, mid+1, e, n)
    }
    if mid == 0 {
        return 0
    } else if end[mid-1] < target{
        return mid- 1 +1
    }
    return binSearchEnd(target,end, s, mid-1,n)


}