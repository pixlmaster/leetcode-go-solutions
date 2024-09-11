class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start < goal:
            start, goal = goal, start
        ans = 0
        while start:
            endBit = start%2
            goalBit = goal%2
            if endBit != goalBit:
                ans += 1
                
            start = start//2
            goal = goal//2
        
        return ans