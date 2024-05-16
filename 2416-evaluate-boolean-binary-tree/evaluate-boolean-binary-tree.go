/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    return dfs(root)
}

func dfs(root *TreeNode) bool {
    if root.Val == 0 {
        return false
    } else if root.Val == 1 {
        return true
    }
    left := dfs(root.Left)
    if root.Val == 3 && !left {
        return false
    }
    right := dfs(root.Right)
    if root.Val == 3 {
        return left && right
    }
    return left || right

}