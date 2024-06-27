class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # iterate over the arrays
        # find the one which has n-1 edges
        freq = {}
        for edge in edges:
            if edge[0] not in freq:
                freq[edge[0]]=1
            else:
                freq[edge[0]]+=1
            
            if edge[1] not in freq:
                freq[edge[1]]=1
            else:
                freq[edge[1]]+=1
        
        n = len(freq)
        for key, val in freq.items():
            if val == (n-1):
                return key
        # print(freq)
        return -1
