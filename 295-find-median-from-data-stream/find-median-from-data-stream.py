class MedianFinder:

    def __init__(self):
        self.minheap = []
        heapq.heapify(self.minheap)
        self.maxheap = []
        heapq.heapify(self.maxheap)
        

    def balance(self) ->None:
        while len(self.minheap) > len(self.maxheap)+1:
            heappush(self.maxheap,-heappop(self.minheap))
        while len(self.maxheap) > len(self.minheap)+1:
            heappush(self.minheap, -heappop(self.maxheap))


    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0:
            heappush(self.minheap,num)
            return
        mintop = self.minheap[0]
        if num >= mintop :
            heappush(self.minheap,num)
        else:
            heappush(self.maxheap,-num)
        self.balance()
        # print("inserted", num)
        # print(self.minheap)
        # print(self.maxheap)
        

    def findMedian(self) -> float:
        if (len(self.minheap) + len(self.maxheap)) & 1 == 0:
            return((self.minheap[0]-self.maxheap[0])/2)
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else :
                return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()