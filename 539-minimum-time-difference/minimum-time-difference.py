class Solution:
    total = 24*60
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        Sort the timepoints
        check diff between point[0] and point[-1]
        check diff between consequtive elements
        """
        timePoints.sort()
        n = len(timePoints)
        diff = float('inf')
        for i in range(n-1):
            curr = self.calcDiff(timePoints[i], timePoints[i+1])
            if curr < diff:
                diff = curr


        curr  = self.calcDiff(timePoints[0], timePoints[-1])
        if curr < diff:
            diff = curr

        return diff



    def calcDiff(self, first : str, last : str)->int :
        firstHour = int(first[:2])
        lastHour = int(last[:2])
        firstMinute = int(first[3:])
        lastMinute = int(last[3:])

        firstTotal = firstHour*60 + firstMinute
        lastTotal = lastHour*60 + lastMinute

        diff = abs(firstTotal - lastTotal)

        return min(diff, self.total-diff)
