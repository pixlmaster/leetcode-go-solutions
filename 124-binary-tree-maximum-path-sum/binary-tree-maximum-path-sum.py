# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def maxProfit(root) -> int:
            nonlocal ans
            if root == None:
                return 0
            leftGain = max(maxProfit(root.left),0)
            rightGain = max(maxProfit(root.right),0)

            currgain = root.val + leftGain+ rightGain
            ans = max(ans,currgain)
            return root.val + max(leftGain,rightGain)

        maxProfit(root)
        return ans	