from bisect import bisect_left


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        # We're looking for a subArr that is of the form k*p + extra
        # calculate preSum, now we need to find two elements whose difference is of the form k*p + extra
        preSum = [0]
        hmap = {0 : [0]}
        ans = 10000000
        for i in range(n):
            preSum.append((preSum[-1]+nums[i])%p)
            if preSum[-1] in hmap:
                hmap[preSum[-1]].append(i+1)
            else:
                hmap[preSum[-1]] = [i+1]
        extra = preSum[-1]
        # print(hmap)
        for key in hmap.keys():
            compl = (key + extra)%p
            if compl not in hmap:
                continue
            # print(key,compl)
            for pos in hmap[key]:
                # possible answers
                toSearch = hmap[compl]
                check = bisect_left(toSearch, pos)
                # if check > 0:
                #     ans = min(ans, abs(pos - toSearch[check -1]))
                if check < len(toSearch):
                    ans  = min(ans, abs(pos - toSearch[check]))
            # 6 , 0, 5, 7
            # 3, 4, 2, 4
        if ans == n:
            return -1
        return ans

