/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func smallestFromLeaf(root *TreeNode) string {
    ans := ""
    visited := make(map[*TreeNode]bool)
    dfs(root,visited,"",&ans)
    return ans

}

func dfs(root *TreeNode, visited map[*TreeNode]bool, curr string, ans *string) {
    isLeaf := root.Left == nil && root.Right == nil
    visited[root] = true
    curr = toString(root.Val) + curr
    if isLeaf {
        if curr < *ans || *ans == "" {
            *ans = curr
        }
    }
    if root.Left != nil {
        val, found := visited[root.Left]
        if !found || !val {
            dfs(root.Left, visited, curr, ans)
        }
    }
    if root.Right != nil {
        val, found := visited[root.Right]
        if !found || !val {
            dfs(root.Right, visited, curr, ans)
        }
    }
    
}

func toString(val int) string{
    return string('a' + val)
}