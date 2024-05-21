class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        num  = pow(2,n)
        ans = []
        for i in range(num) :
            temp = i
            itr = 0
            curr = []
            while temp!=0 :
                if temp%2==1 :
                    curr.append(nums[itr])
                itr = itr + 1
                temp = temp >> 1
            ans.append(curr)
        return ans
            

        