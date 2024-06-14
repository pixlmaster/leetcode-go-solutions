class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # variation of counting sort
        # sort the keys of dict, start from the min value
        # leave 1 , increment all other
        # if incremented key exists, proceed with the loop
        # if incremented key does not exist, next key is the incremented key, and idx ptr remains the same
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        sortedKeys = sorted(freq.keys())
        pickFromSorted = True
        n = len(sortedKeys)
        idx = 0
        curr = -1
        currFreq = -1
        ans = 0
        while idx < n:
            # print(idx, freq)
            if pickFromSorted:
                curr = sortedKeys[idx]
            currFreq = freq[curr]
            # number of elements are at max 1, already unique
            if currFreq <= 1:
                pickFromSorted = True
                idx += 1
                continue
            freq[curr] = 1
            # number of elements are more
            if curr + 1 in freq:
                freq[curr + 1] += currFreq - 1
                idx+=1
                pickFromSorted = True
            else:
                freq[curr + 1] = currFreq - 1
                pickFromSorted = False
                curr = curr + 1
            ans += currFreq - 1
        return ans