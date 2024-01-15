class Solution(object):
    def sumOfLeftLeaves(self, root):
        def findSum(node,isLeft):
            if not node:
                return 0
            ans = 0
            if not node.right and not node.left:
                if isLeft:
                    return node.val
                else:
                    return 0
            elif not node.left:
                return findSum(node.right,False)
            elif not node.right:
                return findSum(node.left,True)
            else:
                return findSum(node.left,True) + findSum(node.right,False)
        return findSum(root,False)
        