class Solution:
    def comp(self, a: List[int], b: List[int])-> int :
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        return 0
            


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=functools.cmp_to_key(self.comp))
        n = len(intervals)
        ans = []
        i=0
        while i<n :
            interval = intervals[i]
            j = i+1
            while j<n:
                tojoin = intervals[j]
                if tojoin[0] <= interval[1]:
                    interval[1] = max(interval[1],tojoin[1])
                else:
                    break
                j+=1
            i=j
            ans.append(interval)


        return ans