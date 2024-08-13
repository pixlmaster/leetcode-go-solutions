from copy import copy


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        # print(candidates)
        self.recurse(candidates, target, ans, 0, [],0)
        # print(ans)
        # Convert each list to a tuple and then use set to remove duplicates
        unique_tuples = set(tuple(lst) for lst in ans)

        # Convert the tuples back to lists
        ans = [list(tup) for tup in unique_tuples]

        return ans

    def recurse(self, candidates: list[int], target: int, ans: list[list[int]], idx: int, curr: list[int], prev: int):
        if target < 0:
            return
        if target == 0:
            currCopy = copy(curr)
            ans.append(currCopy)
            return

        if idx >= len(candidates):
            return

        # don't add candidate
        self.recurse(candidates, target, ans, idx + 1, curr,target)

        if idx > 0 and candidates[idx] == candidates[idx - 1] and prev == target:
            return
        
        # add candidate
        curr.append(candidates[idx])
        self.recurse(candidates, target - candidates[idx], ans, idx + 1, curr, target)
        curr.pop()

        
