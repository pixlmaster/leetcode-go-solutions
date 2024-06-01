class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n)

    def generate(self, n: int) -> set[str]:
        curr = set()
        if n==1:
            curr.add("()")
            return curr
        
        permutations = self.generate(n-1)
        for perm in permutations:
            for itr in range(len(perm)+1):
                copy = perm[:itr] + "()" + perm[itr:]
                curr.add(copy)
        return curr



