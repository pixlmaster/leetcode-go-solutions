import math


class Solution:
    def minSteps(self, n: int) -> int:
        """
        1. FIND THE LARGEST FACTOR -> O(SQrt(n))
        2. minSteps to reach the largest factor
        """
        if n == 1:
            return 0

        largestFactor = n // 2
        while 1:
            if n % largestFactor == 0:
                break
            largestFactor -= 1
        # print(n, largestFactor, n // largestFactor)
        return (n // largestFactor) + self.minSteps(largestFactor)
