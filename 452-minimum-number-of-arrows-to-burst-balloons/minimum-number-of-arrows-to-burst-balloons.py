def compare(a : List[int], b : List[int]) -> int :
    if a[1]<b[1]:
        return -1
    else:
        return 1

class Solution:
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = functools.cmp_to_key(compare))
        end = points[0][1]
        ans = 0
        itr = 0
        for point in points:
            if point[0] > end:
                ans+=1
                end = point[1]
            else:
                end = min(end,point[1])
        return ans + 1