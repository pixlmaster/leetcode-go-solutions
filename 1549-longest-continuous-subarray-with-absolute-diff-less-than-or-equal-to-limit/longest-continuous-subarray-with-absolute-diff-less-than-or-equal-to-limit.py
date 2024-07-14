class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """
        have a min heap
        have a max heap
        have a set of elements
        1.go over nums
        2. put (elem,index) into min heap and max heap, expand right until maxtop - mintop < k
        3. when maxtop - mintop >k
             get maxIndex and minIndex:
                pop the smaller of the two
                pop elements in set from the start till min(maxIndex, minIndex)
                pop elements in maxIndex until the top exists in the set

        """
        minHeap = []
        maxHeap = []
        n = len(nums)

        start = 0
        itr = 0
        ans = 0

        # itr is current index of element
        while itr < n:
            # print("min",minHeap)
            # print("max", maxHeap)
            heapq.heappush(minHeap, (nums[itr],itr))
            heapq.heappush(maxHeap, (-nums[itr],itr))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                start = min(maxHeap[0][1], minHeap[0][1]) +1
                while maxHeap[0][1] < start:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < start:
                    heapq.heappop(minHeap)
                
            ans = max(ans,itr-start+1)
                
            itr += 1
        return ans