class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        targetTime = times[targetFriend][0]
        startMap = {}
        endMap = {}
        n = len(times)
        seats = [-1]*n
        for i in range(n):
            startMap[times[i][0]] = i
            if times[i][1] in endMap:
                endMap[times[i][1]].add(i)
            else:
                endMap[times[i][1]] = set()
                endMap[times[i][1]].add(i)
        # ith candidate is sitting where
        pos = {}
        idx = 0
        for time in range(targetTime+1):
            # first find the leavers
            if time in endMap:
                for i in endMap[time]:
                    if i in pos :
                        # mark the seats empty
                        seats[pos[i]] = -1
                        if pos[i] < idx:
                            idx = pos[i]
                        # remove the positions of the candidates
                        del pos[i]

            # add the newcomer
            if time in startMap:
                while seats[idx] != -1:
                    idx += 1
                # occupy the seat
                seats[idx] = startMap[time]
                pos[startMap[time]] = idx
                if time == targetTime:
                    return idx

        return -1



