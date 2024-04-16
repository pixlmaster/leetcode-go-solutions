/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type queue struct {
    arr []*TreeNode
    front int
    back int
}

func createQueue() *queue{
    return &queue{make([]*TreeNode,10000), 0, 0}
}

func (q *queue) insert(node *TreeNode){
    q.arr[q.back] = node
    q.back++
}

func (q *queue) remove() *TreeNode{
    if q.front == q.back {
        return nil
    }
    q.front++
    return q.arr[q.front-1]
}

func (q *queue) empty() bool{
    return q.front == q.back
}

func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    // corner case
    if depth == 1 {
        return &TreeNode{val, root, nil}

    }
    // level order traversal till depth 
    curr := createQueue()
    curr.insert(root)
    level := 1
    numElems := 1
    for ; level!=depth-1 ; {
        // remove 1 level and enqueue the next one
        currElems :=0
        nextElems :=0
        for ; !curr.empty() && currElems < numElems ; currElems++ {
            node := curr.remove()
            if node.Left != nil {
                curr.insert(node.Left)
                nextElems++
            }
            if node.Right != nil {
                curr.insert(node.Right)
                nextElems++
            }
        }
        numElems = nextElems
        // one level has been traversed
        level++
    }

    for ; !curr.empty(); {
        node := curr.remove()
        left := node.Left
        right := node.Right
        newLeft := &TreeNode{val, left, nil}
        newRight := &TreeNode{val,nil,right}
        node.Left = newLeft
        node.Right = newRight
    }

    return root

}