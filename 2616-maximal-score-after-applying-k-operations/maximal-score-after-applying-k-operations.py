import heapq
import math


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            elem = -heapq.heappop(nums)
            ans += elem
            elem = elem/3
            elem = math.ceil(elem)
            heapq.heappush(nums, -elem)
        
        return ans