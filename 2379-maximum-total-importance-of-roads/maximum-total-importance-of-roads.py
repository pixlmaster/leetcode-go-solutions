class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # create tuples of road, number of edges
        # sort the roads in increasing order of number of edges
        # start assigning the least value from the start
        hmap = {}
        for i in range(n):
            hmap[i] = 0
        for road in roads:
            hmap[road[0]] +=1
            hmap[road[1]] +=1
        roadList = list(hmap.items())
        roadList.sort(key=lambda x: x[1])
        # print(roadList)
        ans = 0
        for i in range(1,n+1):
            ans += roadList[i-1][1]*i
        return ans