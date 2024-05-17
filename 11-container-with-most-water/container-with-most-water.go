func maxArea(height []int) int {
    n := len(height)
    ptr1 := 0
    ptr2 :=n-1
    water := 0
    for ; ptr1 < ptr2 ; {
        minh := min(height[ptr1],height[ptr2])
        curr := (ptr2-ptr1)*minh
        if curr > water {
            water = curr
        }
        if minh == height[ptr1] {
            ptr1++
        } else{
            ptr2--
        }
    }
    return water
}

func min(a,b int) int {
    if a<b {
        return a
    }
    return b
}