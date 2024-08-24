class Solution:
    def nearestPalindromic(self, numStr: str) -> str:
        # find the next largest palindrome
        # find the prev smallest palindrome
        edge_cases = set()
        lenNum = len(numStr)
        for i in range(lenNum + 1):
            edge_cases.add(pow(10, i))
            edge_cases.add(pow(10, i) + 1)

        num = int(numStr)
        if lenNum == 1:
            return str(num - 1)
        elif num in edge_cases:
            n = len(numStr)
            return str(pow(10, n - 1) - 1)

        midPoint = (lenNum - 1) // 2
        half1Str = numStr[:midPoint + 1]
        half2Str = numStr[midPoint + 1:]
        diff = float("inf")
        ans = ""
        if lenNum % 2 == 0:
            # simply copy the first half
            pos3 = half1Str + half1Str[::-1]
            pos3Num = int(pos3)
            if half2Str != half1Str[::-1] and abs(pos3Num - num) < diff:
                ans = pos3
                # print(pos3)
                diff = abs(pos3Num - num)
            half1Num = int(half1Str)
            firstHalfPlus1Str = str(half1Num + 1)
            firstHalfMinus1Str = str(half1Num - 1)
            pos2 = firstHalfPlus1Str + firstHalfPlus1Str[::-1]
            pos2Num = int(pos2)
            if abs(num - pos2Num) < diff:
                # print(pos2)
                ans = pos2
                diff = abs(num - pos2Num)
            pos1 = firstHalfMinus1Str + firstHalfMinus1Str[::-1]
            pos1Num = int(pos1)
            if abs(num - pos1Num) <= diff:
                # print(pos1)
                ans = pos1
                diff = abs(num - pos1Num)
        else:
            # calculate the 2 possibilities
            half1StrWithoutMid = half1Str[:-1]
            midPos1 = int(half1Str[-1]) - 1
            midPos2 = int(half1Str[-1]) + 1
            pos3 = half1StrWithoutMid + str(half1Str[-1]) + half1StrWithoutMid[::-1]
            pos3Num = int(pos3)

            if pos3Num != num and abs(num - pos3Num) < diff:
                ans = pos3
                diff = abs(num - pos3Num)
            if midPos1 >= 0:
                pos1 = half1StrWithoutMid + str(midPos1) + half1StrWithoutMid[::-1]
                pos1Num = int(pos1)
                if abs(num - pos1Num) <= diff:
                    ans = pos1
                    diff = abs(num - pos1Num)

            if midPos2 < 10:
                pos2 = half1StrWithoutMid + str(midPos2) + half1StrWithoutMid[::-1]
                pos2Num = int(pos2)
                if abs(num - pos2Num) < diff:
                    ans = pos2
                    diff = abs(num - pos2Num)

        edgeCaseUpper = pow(10, lenNum) + 1
        edgeCaseLower = pow(10, lenNum - 1) - 1

        if abs(edgeCaseUpper - num) < diff:
            ans = str(edgeCaseUpper)
            diff = abs(edgeCaseUpper - num)
        if abs(edgeCaseLower - num) <= diff:
            ans = str(edgeCaseLower)

        return ans
