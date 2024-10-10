from collections import deque


class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        deq = deque()
        n = len(nums)
        for i in range(n):
            if not deq or nums[i] < nums[deq[-1]]:
                deq.append(i)
        ans = -1
        for i in range(n-1, -1, -1):
            while len(deq) > 0 and nums[deq[-1]] <= nums[i]:
                ans = max(ans, i - deq.pop())
        
        return ans
            

