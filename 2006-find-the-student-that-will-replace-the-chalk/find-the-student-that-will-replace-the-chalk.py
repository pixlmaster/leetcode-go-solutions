class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        chalkSum = sum(chalk)
        k = k%chalkSum
        for i in range(len(chalk)):
            k -= chalk[i]
            if k <0 :
                return i
        return 0
