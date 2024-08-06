class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        """
        find the distinct elements and store them in a set
        """
        freq = {}
        for s in arr:
            if s not in freq:
                freq[s] = 1
            else:
                freq[s] += 1

        unique = set()

        for key in freq.keys():
            if freq[key] == 1:
                unique.add(key)

        if len(unique) < k:
            return ""
        curr = 0
        for s in arr:
            if s in unique:
                curr += 1
                if curr == k:
                    return s

        return ""
