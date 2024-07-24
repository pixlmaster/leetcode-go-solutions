class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        """
        sort using custom comparator
        in the custom comparator function , construct the element from the mapping
        """
        convDict = {}

        def compare(num1: int, num2: int) -> int:
            if num1 == num2:
                return 0
            
            if num1 in convDict:
                conv1 = convDict[num1]
            else :
                conv1 = self.convert(num1, mapping)
                convDict[num1] = conv1

            if num2 in convDict:
                conv2 = convDict[num2]
            else :
                conv2 = self.convert(num2, mapping)
                convDict[num2] = conv2
            # print(num1,conv1)
            # print(num2,conv2)
            if conv1 < conv2:
                return -1
            elif conv1 > conv2:
                return 1
            return 0

        return sorted(nums, key=cmp_to_key(compare))

    def convert(self, num: int, mapping: list[int]) -> int:
        numStr = str(num)
        convArr = []
        for char in numStr:
            charNum = int(char)
            convStr = str(mapping[charNum])
            convArr.append(convStr)

        return int("".join(convArr))