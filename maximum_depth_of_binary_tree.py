class Solution(object):
    def maxDepth(self, root):
        def getHeight(node):
            if node == None:
                return 0
            else:
                return (max(getHeight(node.left),getHeight(node.right)) + 1)
        return getHeight(root)

        