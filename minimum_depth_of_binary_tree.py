class Solution(object):
    def minDepth(self, node):
        if not node:
            return 0
        if not node.right and not node.left:
            return 1
        if not node.left:
            return 1+self.minDepth(node.right)
        if not node.right:
            return 1+self.minDepth(node.left)
        return 1+min(self.minDepth(node.left), self.minDepth(node.right))