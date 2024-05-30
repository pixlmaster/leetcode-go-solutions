class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor = []
        curr = 0
        n = len(arr)
        for elem in arr :
            curr^=elem
            xor.append(curr)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                ij = xor[j-1]
                if i> 0 :
                    ij = ij^xor[i-1]
                for k in range(j,n):
                    jk = xor[j-1] ^ xor[k]
                    if ij == jk:
                        count+=1
        
        return count

        