class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        freqMap = {}
        for i in range(len(target)):
            if target[i] not in freqMap:
                freqMap[target[i]] = 1
            else:
                freqMap[target[i]] += 1

            if arr[i] not in freqMap:
                freqMap[arr[i]] = -1
            else:
                freqMap[arr[i]] -= 1

        for val in freqMap.values():
            if val != 0:
                return False
        return True
