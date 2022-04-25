from pub_module import *
# **********************************************
# 104. Maximum Depth of Binary Tree
# **********************************************
# recursive
def maxDepth(root: [TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
# iterative
def maxDepth(root: [TreeNode]) -> int:
	if not root:
		return 0
	stack = [root]
	depth = 0
	while stack:
		new_stack = []
		for node in stack:
			print(node)
			RC, LC = node.right, node.left
			if RC: new_stack.append(RC)
			if LC: new_stack.append(LC)
		depth += 1
		stack = new_stack
		# explore the new_stack to the end, depth first
		print(new_stack)
	return depth
if __name__=="__main__":
	print('tst')
	
	# 104. Maximum Depth of Binary Tree
	# root = [3,9,20,None,None,15,7],# 3
	# maxDepth(root)
	