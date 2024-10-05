class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        window size of len s1 on s2 and keep checking the count if it equals s1
        """
        s1map = {}
        s2map = {}
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        for i in range(n1):
            if s1[i] in s1map:
                s1map[s1[i]] += 1
            else:
                s1map[s1[i]] = 1

            if s2[i] in s2map:
                s2map[s2[i]] += 1
            else:
                s2map[s2[i]] = 1

        start = 0
        end = n1
        while end <= n2:
            if self.equateMap(s1map, s2map):
                return True
            # print(s2[start:end])
            # print(s2map)
            s2map[s2[start]]-=1
            if end == n2:
                return False
            if s2[end] not in s2map:
                s2map[s2[end]] = 1
            else:
                s2map[s2[end]] += 1
            start += 1
            end += 1

        return False
    def equateMap(self, s1map : dict[str, int], s2map : dict[str, int]) -> bool:
        for key in s1map:
            if key not in s2map:
                return False
            if s1map[key] != s2map[key]:
                return False
            
        return True


