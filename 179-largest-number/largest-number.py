from functools import cmp_to_key


def compare(a: int, b: int) -> int:
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    if ab > ba:
        return -1
    elif ab < ba:
        return 1
    return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        make a map 1- 9
        map[first][numDigits] =
        sort each in descending order
        start from 9 and lowest digits

        """
        hmap = {}
        for i in range(10):
            hmap[str(i)] = []

        for num in nums:
            snum = str(num)
            hmap[snum[0]].append(num)

        for i in range(10):
            hmap[str(i)] = sorted(hmap[str(i)], key=cmp_to_key(compare))
        # print(hmap)
        ans = ""
        for i in range(9,-1,-1):
            for num in hmap[str(i)]:
                ans += str(num)

        return str(int(ans))






