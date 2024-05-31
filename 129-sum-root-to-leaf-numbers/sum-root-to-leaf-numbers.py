# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        self.dfs(root,numbers,0)
        ans =0
        # print(numbers)
        for num in numbers :
            ans+=num
        return ans
    

    def dfs(self, root: TreeNode, numbers : List[int], number : int) :
        if root == None:
            return 
        # leaf node
        leaf = root.left == None and root.right == None 
        if leaf:
            number = number*10 + root.val
            numbers.append(number)
            return
        curr = 10*number + root.val
        # print(curr)
        self.dfs(root.left, numbers, curr)
        self.dfs(root.right, numbers, curr)
        return