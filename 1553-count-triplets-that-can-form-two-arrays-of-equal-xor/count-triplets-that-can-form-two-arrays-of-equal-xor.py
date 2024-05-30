class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor = []
        xor.append(0)
        curr = 0
        for elem in arr :
            curr^=elem
            xor.append(curr)
        # print(xor)
        n = len(xor)

        count = 0
        for i in range(n):
            for j in range(i+1,n):
                # print(xor[i], xor[j])
                if xor[i] == xor[j]:
                    count += j-i-1
        return count

        