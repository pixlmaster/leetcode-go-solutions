class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        idx = self.bin(intervals,newInterval, 0,n-1,n)
        intervals.insert(idx,newInterval)
        self.merge(intervals, idx)
        return intervals

    def bin(self, intervals: List[List[int]],newInterval: List[int], s: int, e : int, n : int) -> int :
        if e < 0 :
            return 0
        if s >= n :
            return n            

        if n==0 :
            return 0
        mid = int((s+e)/2)
        # print(mid)
        search = newInterval[0]
        toCheck = intervals[mid][0]

        # base cases
        if mid == 0:
            if search <= toCheck :
                return 0
            return self.bin(intervals, newInterval, mid+1, e,n)
        # found
        if search <=toCheck :
            if search >= intervals[mid-1][0]:
                return mid
            return self.bin(intervals,newInterval, s, mid-1,n)
        # right side
        if mid == n-1:
            return n
        return self.bin(intervals,newInterval,mid+1,e,n)

    def merge(self, intervals: List[List[int]], idx: int):
        # merge forward
        i = idx+1
        while i < len(intervals) :
            if intervals[i][0] <= intervals[idx][1]:
                intervals[idx][1] = max(intervals[i][1], intervals[idx][1])
                del intervals[i]
            else :
                break
        # merge backwards
        i= idx -1
        while i>= 0 :
            if intervals[idx][0] <= intervals[i][1]:
                intervals[idx][0] = intervals[i][0]
                intervals[idx][1] = max(intervals[i][1], intervals[idx][1])
                del intervals[i]
                idx -= 1
                i -= 1
            else:
                break
        return