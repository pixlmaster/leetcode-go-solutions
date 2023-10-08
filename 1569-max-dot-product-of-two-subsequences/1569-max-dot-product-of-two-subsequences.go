import "fmt"

func maxDotProduct(nums1 []int, nums2 []int) int {
    var prod [501][501]int

    for i:=1 ;i <= len(nums1) ;i++ {
        for j := 1 ; j <= len(nums2); j++{
            currProd := nums1[i-1]*nums2[j-1]
            // base conditions
            // pick 1 and 1
            if i==1 && j==1 {
                prod[i][j] = currProd
            } else if i == 1 {
                // take 1 and j
                prod[i][j] = currProd
                if (prod[i][j-1] > prod[i][j]){
                    prod[i][j] = prod[i][j-1]
                }
            } else if j==1 {
                // take 1 and j
                prod[i][j] = currProd
                if (prod[i-1][j] > prod[i][j]){
                    prod[i][j] = prod[i-1][j]
                }
            }
            
            if i!=1 && j!=1 {
                if currProd > 0 {
                    // take both
                    prod[i][j] = prod[i-1][j-1] + currProd
                } else {
                    // dont take both
                    prod[i][j] = prod[i-1][j-1]
                }
                // fresh start
                if currProd > prod[i][j] {
                    prod[i][j] = currProd
                }

                if prod[i][j] < prod[i-1][j] {
                    // take  max and j
                    prod[i][j] = prod[i-1][j]
                }
                if prod[i][j] < prod[i][j-1] {
                    // take i and max
                    prod[i][j] = prod[i][j-1]
                }
                
            }

        }
    }
    
    return prod[len(nums1)][len(nums2)]

}