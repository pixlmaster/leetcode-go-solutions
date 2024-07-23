class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        """
        stored values in hashmap and zip it along with the current elem
        sort acc to frequency, if frequency same then decreasing order of freq
        """
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

        def compare(x: int, y: int) -> int:
            if freqMap[x] < freqMap[y]:
                return -1
            elif freqMap[x] > freqMap[y]:
                return 1
            if x < y:
                return 1
            elif x>y:
                return -1
            return 0
        return sorted(nums, key=cmp_to_key(compare))