class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        create a list of tuples (x,freq)
        sort in decreasing order of freq
        start assigning from the end

        map 2-9 - []
        currNum = 2
        map [letter]cost
        if char not in map:
            map[char] = len(mapNum[curr])
            curr+=1
            if curr == 10:
                curr = 2
            ans = map[char]
        else:
            ans = map[char]
        """

        freq = {}
        mapping = {}
        cost = {}

        for i in range(2, 10):
            mapping[i] = 0

        for char in word:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        sorted_tuples = []

        for key in freq.keys():
            sorted_tuples.append((key, freq[key]))

        sorted_tuples.sort(key=lambda x: x[1], reverse=True)

        # print(sorted_tuples)
        curr = 2
        ans = 0
        for tup in sorted_tuples:
            char = tup[0]
            if char in cost:
                ans += tup[1] * cost[char]
            else:
                mapping[curr] += 1
                cost[char] = mapping[curr]
                curr += 1
                ans += tup[1] * cost[char]
                if curr == 10:
                    curr = 2

        return ans
