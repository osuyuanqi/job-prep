# ***********************************************
# 101. Symmetric Tree
# ***********************************************

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def tst(rootleft,rootright):
        if rootleft == None or rootright==None:
            return rootleft==rootright
        return rootleft.val ==rootleft.val and tst(rootleft.left,rootright.right) and tst(rootleft.right,rootright.left)
        
    return tst(root.left,root.right)

# ***********************************************
# 108. Convert Sorted Array to Binary Search Tree
# ***********************************************

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) ==0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right =  self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__=="__main__":
    print('tst')
