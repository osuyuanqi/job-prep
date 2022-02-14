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
        # stack stores all the leftnodes
        while root:
            stack.append(root)
            root = root.left
        print(stack)
        # pop the current node only, without the rest tree
        # do pop() each iteration
        node = stack.pop()
        res.append(node.val)
        # explore the right ROOT, not node
        root = node.right
    return res
# **********************************************
# 145. Binary Tree Postorder Traversal
# **********************************************

# recursive
def postorderTraversal(self, root: [TreeNode]) -> List[int]:
	def post_order(root, res):
	    if root:
	        post_order(root.left,res)
	        post_order(root.right,res)
	        res.append(root.val)
	r = []
	post_order(root, r)
	return r
# **********************************************
#102. Binary Tree Level Order Traversal
# **********************************************





if __name__ == "__main__":
	# root = [1,None,2,3]
	# inorderTraversal_recursive(root)
	print("test")
