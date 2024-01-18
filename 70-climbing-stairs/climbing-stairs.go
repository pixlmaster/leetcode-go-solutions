func climbStairs(n int) int {
    // base condition
    if n == 1 {
        return 1
    }
    // no of ways to reach the prev step
    step1Before := 1
    // no of ways to reach the step before the prev step
    step2Before := 1

    var steps int
    for i := 2 ;i <=n ;i ++ {
        // ways of reaching step  = ways of reaching prev step + ways of reaching the step before prev step
        steps = step1Before + step2Before
        // for next iteration
        // step 2 before becomes step 1 before
        step2Before = step1Before
        // step 1 before becomes current
        step1Before = steps
    }

    return steps
}