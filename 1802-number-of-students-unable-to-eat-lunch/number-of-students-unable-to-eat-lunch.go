func countStudents(students []int, sandwiches []int) int {
    n := len(students)
    unable := n
    prevUnable :=-1
    for i,j :=0,0 ; i<n ; {
        // fmt.Println(i,j)
        if sandwiches[i] == students[j] {
            students[j] = -1
            unable--
            i++
            j++
        } else{
            j++
        }

        if(j==n) {
            j = 0
            if prevUnable == unable {
                break
            }
            prevUnable = unable
        }
    }
    return unable
}