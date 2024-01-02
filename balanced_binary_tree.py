class Solution(object):
    def isBalanced(self, root):
        self.check = True
        def checkTree(root):
            if not root:
                return 0
            l,r = checkTree(root.left) , checkTree(root.right)
            if self.check:
                self.check = abs(l-r)<=1
            return (max(l,r)+1)
        checkTree(root)
        return self.check

        