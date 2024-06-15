class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # sorted profits acc to capital
        # sorted capital
        # gain = profit
        # put all elements in the sortedcapital(gains) up until currentcapital into the max heap
        # pop the gain add it to the weight, add more elements to the heap

        zippedList = zip(capital,profits)
        sortedZipped = sorted(zippedList)
        ptr = 0
        count =0
        heap = []
        currCapital = w
        while count < k:
            while ptr < len(profits) and sortedZipped[ptr][0] <= currCapital:
                # insert the possible into the heap
                heapq.heappush(heap,-sortedZipped[ptr][1])
                ptr+=1
            
            if len(heap) == 0:
                break
            
            maxGain = -heapq.heappop(heap)
            currCapital += maxGain
            count+=1
        
        return currCapital
        