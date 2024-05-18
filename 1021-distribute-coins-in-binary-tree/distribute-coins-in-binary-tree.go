/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type ExtraNode struct {
    val int
    left *ExtraNode
    right *ExtraNode
    numLeft int
    numRight int
    gleft int
    gright int
}

func constructTree(root *TreeNode) *ExtraNode{
    if root == nil {
        return nil
    }
    extraRoot := &ExtraNode {
        root.Val,
        nil,
        nil,
        0,
        0,
        0,
        0,
    }
    if root.Left!=nil {
        // if left node exists
        extraRoot.left = constructTree(root.Left)
        extraRoot.numLeft = extraRoot.left.numLeft + extraRoot.left.numRight + 1
        extraRoot.gleft = extraRoot.left.gleft + extraRoot.left.gright + extraRoot.left.val
    }
    if root.Right!=nil {
        extraRoot.right = constructTree(root.Right)
        extraRoot.numRight = extraRoot.right.numLeft + extraRoot.right.numRight + 1
        extraRoot.gright = extraRoot.right.gleft + extraRoot.right.gright + extraRoot.right.val
    }
    
    // fmt.Println("constructed extraRoot ", extraRoot)

    return extraRoot


}

func dfs(root *ExtraNode) int {
    if root == nil {
        return 0
    }
    lexcess := root.gleft - root.numLeft
    rexcess := root.gright - root.numRight
    // fmt.Println("root ", root)
    // fmt.Println("root val ", root.val)
    // fmt.Println("left " ,lexcess)
    // fmt.Println("right " ,rexcess)
    // base case, current node has 1 coin and left and right subtree have enough to handle themselves
    if root.val == 1 && lexcess == 0 && rexcess == 0 {
        return dfs(root.left) + dfs(root.right)
    }
    moved :=0 
    // move coins from right/root to left
    if lexcess <0 {
        deficit := -lexcess
        moved += deficit
        // move from root
        root.val -= deficit
        root.gleft += deficit
        root.left.val +=deficit
        // re -enter from root
        return moved + dfs(root)
    }
    if rexcess < 0 {
        deficit := -rexcess
        moved += deficit
        // move from root
        root.val -= deficit
        root.gright += deficit
        root.right.val += deficit
        // re -enter from root
        return moved + dfs(root)
    }
    curr := root.val
    // curr reaches a deficit for providing one of the childrens
    if curr <= 0 {
        deficit := 1 - root.val
        moved += deficit
        // take from excess child
        if lexcess >0 {
            // take only the availaible ones
            if deficit > lexcess {
                root.gleft -= lexcess
                root.left.val -= lexcess
                root.val += lexcess
            } else {
                root.left.val -= deficit
                root.gleft -= deficit 
                root.val +=deficit
            } 
        }
        deficit = 1 - root.val
        if rexcess >0 {
            root.right.val -= deficit
            root.gright -= deficit 
        }
        root.val = 1

    }
    return moved + dfs(root)
}

func distributeCoins(root *TreeNode) int {
    root1 := constructTree(root)
    return dfs(root1)
}
