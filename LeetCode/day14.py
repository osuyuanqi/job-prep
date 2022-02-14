from pub_module import *
# **********************************************
# 94. Binary Tree Inorder Traversal
# **********************************************

# recursive way
def inorderTraversal_recursive(root: [TreeNode]) -> list[int]:
    def traversal(root,res):
        if root:
            traversal(root.left, res)
            res.append(root.val)
            traversal(root.right,res)
    r = []
    traversal(root,r)
    return r

# iterative way
def inorderTraversal_iterative(root: [TreeNode]) -> list[int]:
    res, stack = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        print(stack)
        # pop the node only, without the rest tree
        node = stack.pop()
        res.append(node.val)
        # explore the right node
        root = node.right
    return res

if __name__ == "__main__":
	# root = [1,None,2,3]
	# inorderTraversal_recursive(root)
	print("test")
