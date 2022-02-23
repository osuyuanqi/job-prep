from pub_module import TreeNode
# **********************************************
# 724. Find Pivot Index
# function sum tips
# **********************************************

# method1: math tip
def pivotIndex(self, nums: list[int]) -> int:
    total = sum(nums)
    lsum = 0
    for i in range(len(nums)):
        rsum = total - lsum - nums[i]
        if lsum == rsum:
            return i
        lsum += nums[i]
    return -1

# method2: use function
def pivotIndex(self, nums: list[int]) -> int:
    #Error case 
    if nums == None: return -1
    #base case 
    if len(nums) == 0: return -1 
    if len(nums) == 1: return 0
    if len(nums) == 2: return -1
    #iterations 
    for i in range(len(nums)):
        left_sum = sum(nums[0:i])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
    return -1
# **********************************************
# 112. Path Sum
# **********************************************

def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
    if root == None:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    return  self.hasPathSum(root.left,targetSum - root.val) or self.hasPathSum(root.right, targetSum -root.val)
# **********************************************
# 104. Maximum Depth of Binary Tree
# **********************************************

 def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


if __name__ == "__main__":
	print('test')