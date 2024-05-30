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
                ij = curr
                jn = curr^xor[j-1]
                ij^=jn
                if i> 0 :
                    ij = ij^xor[i-1]
                for k in range(j,n):
                    k1n = curr ^ xor[k]
                    jk = curr ^ xor[j-1] ^ k1n
                    if ij == jk:
                        # print(i,j,k,ij,jk)
                        count+=1
        
        return count

        