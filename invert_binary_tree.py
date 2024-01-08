class Solution(object):
    def invertTree(self, root):
        def invert(root):
            if root == None:
                return None
            else:
                temp = root.right
                root.right = root.left
                root.left = temp
                invert(root.left)
                invert(root.right)
                return root
        invert(root)
        return root