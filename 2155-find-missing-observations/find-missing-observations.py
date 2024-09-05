class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        currSum = sum(rolls)
        expectedSum = (m+n)*mean
        if currSum + n > expectedSum or currSum + 6*n < expectedSum:
            return []
        remainingSum = expectedSum - currSum
        initValue = remainingSum // n
        ans = [initValue]*n
        remainder = remainingSum - initValue*n
        currItr = 0
        while remainder > 0:
            if ans[currItr] + remainder >6 :
                remainder -= 6- ans[currItr]
                ans[currItr] = 6
                currItr+=1
            else :
                ans[currItr] += remainder
                break

        return ans

    