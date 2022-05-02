from pub_module import TreeNode
# **********************************************
# 217. Contains Duplicate
# **********************************************
def containsDuplicate(nums: list[int]) -> bool:
	s=set()
	for i in nums:
		if i in s:
			return True
		s.add(i)
	return False
def containsDuplicate(nums: list[int]) -> bool:
	return len(set(nums))!=len(nums)

# **********************************************
# 268. Missing Number
# **********************************************
def missingNumber(nums: list[int]) -> int:
	nums = set(nums)
	a=0
	for i in range(len(nums)+1):
		a+=i
	return a-sum(nums)
def missingNumber(nums: list[int]) -> int:
	nums = set(nums)
	for i in range(len(nums)):
		if i not in nums:
			return i
# math
def missingNumber(nums: list[int]) -> int:
	n = len(nums)
	return (n)*(n+1)//2-sum(nums)
# slower
def missingNumber(nums: list[int]) -> int:
	nums = set(nums)
	for i in nums:
		nums.add(i)
	for i in range(len(nums)+1):
		if i not in nums:
			return i
# **********************************************
# 387. First Unique Character in a String
# **********************************************
def firstUniqChar(s: str) -> int:
	dic,arr={},{}
	for i in range(len(s)):
		if s[i] not in dic:
			dic[s[i]]=1
			arr[s[i]]=i
		else:
			dic[s[i]]+=1
	# print(dic,arr)
	for k,v in dic.items():
		# print(k,v)
		if v==1:
			return arr[k]
	return -1
# store a list in dic
def firstUniqChar(s: str) -> int:
	dic={}
	for i in range(len(s)):
		if s[i] not in dic:
			dic[s[i]]=[1,i]
		else:
			dic[s[i]]=2
	# print(dic,arr)
	for k,v in dic.items():
		if v!=2:
			return v[1]
	return -1
# **********************************************
# 108. Convert Sorted Array to Binary Search Tree
# **********************************************

def sortedArrayToBST(nums: list[int]) -> [TreeNode]:
    if len(nums)==0: return None
    mid = len(nums)//2
    root=TreeNode(nums[mid])
    # print(root)
    root.left=self.sortedArrayToBST(nums[:mid])
    root.right=self.sortedArrayToBST(nums[mid+1:])
        
    return root
# **********************************************
# 21. Merge Two Sorted Lists
# **********************************************
def mergeTwoLists(list1: [ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		# same object, one pointer move, another pointer stay
        dummy=p=ListNode(-1)
        while list1 and list2:
            if list1.val>list2.val:
                dummy.next=list2
                list2=list2.next
            else:
                dummy.next=list1
                list1=list1.next
            dummy=dummy.next
        if list1:
            dummy.next=list1
        if list2:
            dummy.next=list2
        return p.next
if __name__=="__main__":
	print('tst')
	# 217. Contains Duplicate
	# nums = [1,2,3,1]
	# print(containsDuplicate(nums))

	# 268. Missing Number
	# nums=[9,6,4,2,3,5,7,0,1]
	# print(missingNumber(nums))

	# 387. First Unique Character in a String
	# s = "aabbc"
	# print(firstUniqChar(s))