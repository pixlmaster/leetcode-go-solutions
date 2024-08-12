import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapq.heapify(nums)
        self.heap = nums
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == 0 or len(self.heap) <self.k or val > self.heap[0]:
            heapq.heappush(self.heap,val)
            while len(self.heap) > self.k:
                heapq.heappop(self.heap)
            return  self.heap[0]
        else:
            return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
