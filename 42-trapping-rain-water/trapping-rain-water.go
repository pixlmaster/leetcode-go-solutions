func trap(height []int) int {
    n := len(height)
    leftMax := make([]int,n)
    rightMax := make([]int,n)

    leftMax[0] = height[0]
    for i := 1 ; i< n ; i++ {
        if height[i] > leftMax[i-1] {
            leftMax[i] = height[i]
        } else {
            leftMax[i] = leftMax[i-1]
        }
    }
    prev := height[n-1]
    water := min(prev,leftMax[n-1]) - height[n-1]
    for i := n-2 ; i>= 0 ; i-- {
        if height[i] > prev {
            water += min(height[i],leftMax[i]) - height[i]
            rightMax[i] = height[i]
            prev = height[i]
        } else {
            water += min(prev,leftMax[i]) - height[i]
        }
    }
    return water

}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}