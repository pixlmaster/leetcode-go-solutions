import heapq


class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        store index of 1st 1 index ecountered, if none return 0
        for every 1 you encounter,
        ams += stored index
        stored index = current index
        """
        lastIdx = -1
        n = len(s)
        swaps = 0
        heapIdx = []
        for idx in range(n):
            # print(idx, s[idx], heapIdx)
            if lastIdx < 0 :
                if s[idx] == '1':
                    lastIdx = idx
                    heapq.heappush(heapIdx, idx)
            else :
                if s[idx] == '0':
                    if len(heapIdx) == 0 :
                        continue
                    lastIdx = heapq.heappop(heapIdx)
                    swaps += idx - lastIdx
                    heapq.heappush(heapIdx, idx)
                else:
                    heapq.heappush(heapIdx, idx)
        return swaps