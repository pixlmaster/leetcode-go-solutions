func compareVersion(version1 string, version2 string) int {
    n1 := len(version1)
    n2 := len(version2)
    // make n2 always larger
    // if n2<n1 {
    //     temp:= version1
    //     t := n1
    //     version1 = version2
    //     version2 = temp
    //     n1 = n2
    //     n2 = t
    // }


    for i1,i2:=0,0 ; i2< n2 || i1<n1; {
        curr1 := ""
        curr2 := ""
        for ; i1<n1 && version1[i1]!='.' ; i1++{
            curr1 += string(version1[i1])
        }
        for ; i2<n2 && version2[i2]!='.'  ; i2++{
            curr2 += string(version2[i2])
        }
        // edge case handling
        if curr1 == "" {
            curr1 = "0"
        }

        if curr2 == "" {
            curr2 = "0"
        }
        int1, _ := strconv.Atoi(curr1)
        int2, _ := strconv.Atoi(curr2)

        if int1 > int2 {
            return 1
        } else if int2 > int1{
            return -1
        }
        i1++
        i2++
    }

    return 0
    
}