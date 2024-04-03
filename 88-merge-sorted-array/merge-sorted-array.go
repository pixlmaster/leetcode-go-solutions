func merge(nums1 []int, m int, nums2 []int, n int)  {
    merged := make([]int, m + n)
    i := 0
    j := 0
    for ;i < m && j < n ;{
        if nums1[i] < nums2[j] {
            merged[i+j] = nums1[i]
            i++
        } else {
            merged[i+j] = nums2[j]
            j++
        }   
    }

    if i==m{
        for ; j<n ; j++ {
            merged[m + j] = nums2[j]
        }
    } else {
            for ; i<m ; i++ {
            merged[n + i] = nums1[i]
        }
    }

    for i = 0 ;i < m + n ; i++ {
        nums1[i] = merged[i]
    }

}