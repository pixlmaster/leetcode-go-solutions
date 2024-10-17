class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        2736
        9973
        Find the first number whose next number is greater than the current - this is the number ot be replaced
        Find the greatest number from this index onwards, replace it with this
        """
        numStr = str(num)
        toReplace = -1
        swapIdx = -1
        for i in range(len(numStr)-1):
            if toReplace < 0 and numStr[i] < numStr[i+1]:
                toReplace = i
                swapIdx = i + 1
                break
        if toReplace == -1 or swapIdx == -1 :
            return num

        # find the greatest element from swapidx+1 to end

        for i in range(swapIdx+1, len(numStr)):
            if numStr[i] >= numStr[swapIdx]:
                swapIdx = i

        # find the first element from start which is smaller thans swapIdx
        for i in range(0, swapIdx+1):
            if numStr[i] < numStr[swapIdx]:
                toReplace = i
                break
        
        # print(toReplace,swapIdx)

        return int(numStr[:toReplace] + numStr[swapIdx]+numStr[toReplace+1:swapIdx]+numStr[toReplace] + numStr[swapIdx+1:])