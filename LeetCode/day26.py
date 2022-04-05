from pub_module import TreeNode
# ***********************************************
# 101. Symmetric Tree
# ***********************************************

def isSymmetric(self, root: [TreeNode]) -> bool:
    def tst(rootleft,rootright):
        if rootleft == None or rootright==None:
            return rootleft==rootright
        return rootleft.val ==rootleft.val and tst(rootleft.left,rootright.right) and tst(rootleft.right,rootright.left)
        
    return tst(root.left,root.right)

# ***********************************************
# 66. Plus One
# ***********************************************

def sortedArrayToBST(self, nums: list[int]) -> [TreeNode]:
        if len(nums) ==0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right =  self.sortedArrayToBST(nums[mid+1:])
        return root

# ***********************************************
# 108. Convert Sorted Array to Binary Search Tree
# ***********************************************

# way1: map
def plusOne(digits: list[int]) -> list[int]:
    st = ''.join(map(str,digits))
    b = int(st)+1
    digits = list(map(int,str(b)))
    return digits

# way2: step by step conversion
def plusOne1(digits: list[int]) -> list[int]:
    a=[str(i) for i in digits]
    b = int(''.join(a))+1
    c=[int(i) for i in str(b)]
    return c

# way3: concentrate the last digit only
def plusOne2(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            i -= 1
    return [1] + digits

if __name__=="__main__":
    print('tst')
    
    # 66. Plus One
    # digits = [8,9]#[9,9]->[1,0,0],[4,3,2,1]->[4,3,2,2]
    # print(plusOne(digits))