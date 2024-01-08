class Solution(object):
    def isSameTree(self, p, q):
        def checkNodes(node1,node2):
            if node1 == None:
                return node2 == None
            elif node2 == None:
                return node1==None
            return node1.val == node2.val and checkNodes(node1.left,node2.left) and checkNodes(node1.right, node2.right)
        return checkNodes(p,q)
        