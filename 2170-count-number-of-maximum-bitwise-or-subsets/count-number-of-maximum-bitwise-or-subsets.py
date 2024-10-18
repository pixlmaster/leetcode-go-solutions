class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        toCheck = 0
        for i in range(n):
            toCheck = toCheck | nums[i]

        limit = pow(2, n)
        ans = 0
        for i in range(limit):
            c = i
            curr = 0
            idx = 0
            while c!=0:
                if c % 2 == 1:
                    curr = curr | nums[idx]
                idx+=1
                c = c//2
            if curr == toCheck:
                ans +=1

        return ans