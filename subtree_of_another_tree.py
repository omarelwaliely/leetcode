class Solution(object):
    def isSubtree(self, root, subRoot):
        def checkMore(mainNode, subNode):
            if not mainNode and not subNode:
                return True
            elif not mainNode or not subNode:
                return False
            elif mainNode.val == subNode.val:
                return checkMore(mainNode.left, subNode.left) and checkMore(mainNode.right, subNode.right)
            else:
                return False
        def checkSubtree(mainNode, subNode):
            if not mainNode:
                return False
            elif mainNode.val == subNode.val and checkMore(mainNode, subNode):
                return True
            else:
                return checkSubtree(mainNode.left, subNode) or checkSubtree(mainNode.right, subNode)
        return checkSubtree(root,subRoot)