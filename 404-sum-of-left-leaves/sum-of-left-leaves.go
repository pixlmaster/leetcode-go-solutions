/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    return recurse(root,false)
}

func recurse(root *TreeNode, isLeft bool) int {
    isLeaf := root.Left == nil && root.Right == nil

    if isLeaf && isLeft{
        return root.Val
    }

    ans := 0

    if root.Left!=nil {
        ans += recurse(root.Left, true)
    }

    if root.Right!=nil {
        ans += recurse(root.Right, false)
    }

    return ans

}