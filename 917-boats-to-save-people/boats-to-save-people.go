func numRescueBoats(people []int, limit int) int {
    sort.Ints(people)
    n:= len(people)
    ptr1 := 0 
    ptr2 := n-1
    boats:=0

    for ; ptr1<=ptr2 ; {
        sum := people[ptr1] + people[ptr2]
        if ptr1 == ptr2 {
            sum = people[ptr1]
        }
        if  sum > limit{
            ptr2--
            boats++
        } else {
            ptr1++
            ptr2--
            boats++
        }
    }
    return boats
}