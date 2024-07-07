class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emptyBottles = 0
        totalBottles = numBottles
        fullBottles = numBottles
        while fullBottles:
            # drink the full bottles
            ans+=fullBottles
            # calculate number of empty bottles, full ones become empty
            emptyBottles += fullBottles
            # convert empty into full bottles
            fullBottles = emptyBottles//numExchange
            # calculate the number of emptyBottles left now
            emptyBottles =emptyBottles%numExchange
            # calculate total bottles
            totalBottles = fullBottles + emptyBottles
        return ans