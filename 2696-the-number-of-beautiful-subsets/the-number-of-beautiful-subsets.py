class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        kmap = {}
        for num1 in nums:
            kmap[num1] = []
            for index, num2 in enumerate(nums):
                if self.diff(num1,num2) == k:
                    kmap[num1].append(index)
        print(kmap)
        ans = 0

        elems  = pow(2,n)
        for i in range(1,elems) :
            pickable = [True]*n
            picked = True
            itr = 0
            ci = i
            while ci>0 :
                if ci%2 == 1 :
                    if pickable[itr] :
                        for ridx in kmap[nums[itr]] :
                            pickable[ridx] = False
                    else :
                        picked = False
                        break
                ci = ci >> 1
                itr = itr +1
            if picked :
                ans = ans +1
        return ans

    def diff(self, a : int, b: int) -> int :
        diff = a-b
        if diff<0 :
            return -diff
        return diff
    