class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack pick an element, do not pick an element
        # if sum <0
        # return and do not add the answer
        # if sum  >0. try picking more
        # sum==0, found one answer
        # only allowed to pick elements at idx or ahead
    
        ans =[]
        
        self.combine(candidates,0,target,[],ans)
        
        return ans

    def combine(self, candidates: List[int],idx:int, target:int , comb : List[int], ans :List[List[int]]) ->None:
        if target == 0:
            ans.append(copy.deepcopy(comb))
            return
        if target <0 or idx >= len(candidates):
            return
        # do not pick the element move idx ahead
        self.combine(candidates,idx+1,target,comb,ans)
        comb.append(candidates[idx])
        # pick element and keep idx here only
        self.combine(candidates,idx,target - candidates[idx], comb,ans)
        comb.pop()