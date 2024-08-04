class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        """
        calculate prefix sum
        pick any i,j(j>i), subtract them to get the subarray sum, append it in a list
        sort the list
        """
        mod = pow(10,9) +7
        prefixSum =[0]
        for i,num in enumerate(nums):
            prefixSum.append(prefixSum[i]+num)

        # print(prefixSum)
        n = len(prefixSum)
        sumList =[]
        for i in range(n):
            for j in range(i+1,n):
                sumList.append(prefixSum[j] - prefixSum[i])

        sumList.sort()
        # print(sumList)
        ans = 0
        while left <= right:
            ans += sumList[left-1]
            ans = ans % mod
            left+=1
        
        return ans
