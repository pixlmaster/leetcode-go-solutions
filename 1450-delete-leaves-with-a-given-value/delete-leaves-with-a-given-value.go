/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    removeLeafNodesWithParent(root,root,target)
    // corner case
    if root.Left == nil && root.Right == nil && root.Val == target {
        return nil
    }

    return root
}

func removeLeafNodesWithParent(root *TreeNode,parent *TreeNode, target int) {
    if root == nil {
        return 
    }

    removeLeafNodesWithParent(root.Left,root, target)
    removeLeafNodesWithParent(root.Right,root, target)
    // Delete the leaf
    if root.Left == nil && root.Right == nil && root.Val == target {
        // fmt.Println("Deleting ", root.Val , "Parent ", parent.Val)
        if parent.Left == root {
            parent.Left = nil
        } else{
            parent.Right = nil
        }
    } 

}