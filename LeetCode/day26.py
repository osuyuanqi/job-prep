# ***********************************************
# 101. Symmetric Tree
# ***********************************************

def compare(self,root1,root2):
	if root1==None or root2==None:
	    return root1==root2
	return root1.val == root2.val and self.compare(root1.left, root2.right) and self.compare(root1.right, root2.left)
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return self.compare(root.left, root.right)

if __name__=="__main__":
    print('tst')
    