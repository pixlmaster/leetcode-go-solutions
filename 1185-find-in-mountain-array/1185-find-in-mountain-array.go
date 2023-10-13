/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 *
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */

func fetchFromMountainArr(idx int, mountainArr *MountainArray, acc map[int]int) int {
    _, ok := acc[idx]
    if !ok {
        acc[idx] = mountainArr.get(idx)
    }
    return acc[idx]
}

func findInMountainArray(target int, mountainArr *MountainArray) int {
    acc := make(map[int]int)
    n := mountainArr.length()
    min1 := fetchFromMountainArr(0, mountainArr, acc)
    min2 := fetchFromMountainArr(n-1, mountainArr, acc)
    // target is less than the minimum value in the arr
    if(target < min1  && target < min2){
        return -1
    }

    // fint the peak of the mountain
    peak := findPeak(mountainArr, 0, n-1, n,acc)

    // target is greater than max value in the arr
    if target > fetchFromMountainArr(peak,mountainArr, acc) {
        return -1
    }


    // peak is the target
    if target == fetchFromMountainArr(peak,mountainArr, acc) {
        return peak
    }

    // search on both sides of the peak
    peakLeft := binSearch(mountainArr, 0, peak-1,target,acc, true)
    if peakLeft != -1 {
        return peakLeft
    }
    return binSearch(mountainArr, peak+1, n-1,target,acc,false)

}

func findPeak(mountainArr *MountainArray , l int, r int,n int, acc map[int]int) int {
    if( l > r || l < 0 || r >=n  ){
        return -1
    }
    mid := ( l + r )/2

    midElem := fetchFromMountainArr(mid, mountainArr,acc)

    // corner cases
    if mid == 0 {
        return findPeak(mountainArr, mid+1,r,n,acc)
    } else if mid == n-1 {
        return findPeak(mountainArr, l, mid - 1, n, acc)
    } else {
        midLeft := fetchFromMountainArr(mid-1, mountainArr,acc)
        // search on left side
        if midElem < midLeft {
            return findPeak(mountainArr, l, mid-1, n,acc)
        } 
        midRight := fetchFromMountainArr(mid+1, mountainArr,acc)

        // found peak
        if midElem > midLeft && midElem > midRight {
            return mid
        }
        // search on right side
        return findPeak(mountainArr,mid+1,r,n,acc)

    } 
}

func binSearch(mountainArr *MountainArray, l int, r int , target int, acc map[int]int, asc bool) int {
    if l > r  {
        return -1
    }
    mid := ( l + r )/2

    midElem := fetchFromMountainArr(mid, mountainArr,acc)

    if midElem == target {
        return mid
    } else if target < midElem {
        if asc {
            return binSearch(mountainArr,l, mid-1, target,acc, asc)
        } else {
            return binSearch(mountainArr,mid+1, r, target,acc, asc)
        }
    } else {
        if asc {
            return binSearch(mountainArr,mid+1, r, target,acc,asc)
        } else {
            return binSearch(mountainArr,l, mid-1, target,acc,asc)
        }
    }
}